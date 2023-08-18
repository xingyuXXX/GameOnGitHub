import os.path
import sys
import tkinter as tk
from PIL import ImageTk, Image

app_lang = 'zh'


def get_resource_path(img_file):
    relative_path = os.path.join('weapons', img_file)
    if hasattr(sys, '_MEIPASS'):  # for PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


class WeaponsRotationSimulator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aphelios Weapons Rotation Simulator")

        self.frm_weapons = tk.Frame()
        self.frm_buttons = tk.Frame()
        self.frm_orders = tk.Frame()
        self.frm_weapons.pack()
        self.frm_buttons.pack()
        self.frm_orders.pack()

        self.calibrum = Weapon("Calibrum", '通碧', get_resource_path('Calibrum.png'), "green")
        self.severum = Weapon("Severum", '断魄', get_resource_path('Severum.png'), "red")
        self.gravitium = Weapon("Gravitium", '坠明', get_resource_path('Gravitium.png'), "purple")
        self.infernum = Weapon("Infernum", '荧焰', get_resource_path('Infernum.png'), "blue")
        self.crescendum = Weapon("Crescendum", '折镜', get_resource_path('Crescendum.png'), "white")

        self.init_color_order = ['green', 'red', 'purple', 'blue', 'white']
        self.cur_color_order = self.init_color_order[:]
        self.prev_color_order = self.init_color_order[:]
        self.selected_order = []

        self.btns_weapon = []
        for i, wp_color in enumerate(self.init_color_order):

            if i in [0, 1]:  # does not work on macOS
                bg_color = '#add8e6'
            else:
                bg_color = None

            button = tk.Button(master=self.frm_weapons,
                               text=self.get_weapon_by_color(wp_color).name,
                               compound=tk.BOTTOM,  # image below text
                               fg=wp_color,
                               bg=bg_color,
                               image=self.get_weapon_by_color(wp_color).img,
                               font=("Open Sans", 20),
                               height=320,
                               width=280)

            button.grid(row=0, column=i)

            if i in [0, 1]:
                button.config(state=tk.NORMAL, command=lambda p=i: self.handler_consume(p))
                if i == 1:
                    button.grid(row=0, column=i, padx=(0, 40))
            else:
                button.config(state=tk.DISABLED)

            self.btns_weapon.append(button)

        tk.Button(master=self.frm_buttons, text="Reset", font=('Open Sans', 20), command=self.handler_reset).grid(row=0, column=0)
        tk.Button(master=self.frm_buttons, text="Undo", font=('Open Sans', 20), command=self.handler_undo).grid(row=0, column=1)
        tk.Button(master=self.frm_buttons, text="Set Order", font=('Open Sans', 20),
                  command=self.handler_set_order).grid(row=0, column=2, padx=(20, 0))

        tk.Label(master=self.frm_orders, text="Desired Weapons Combo:", font=('Open Sans', 20)).grid(row=0, column=0, columnspan=2, pady=(20, 0))
        tri_combos = ['蓝白红', '红白绿']
        self.dict_combos = []

        for i, combo in enumerate(tri_combos):
            btn = (tk.Button(master=self.frm_orders, text=combo, font=('Open Sans', 20),
                             command=lambda o=combo: self.handler_desired(o)))
            btn.grid(row=i+1, column=0)
            lbl = tk.Label(master=self.frm_orders, font=('Open Sans', 20))
            lbl.grid(row=i+1, column=1)

            self.dict_combos.append({'btn': btn, 'lbl': lbl, 'combo': combo})

    def determine_consuming_order(self, desired_combo) -> str:
        on_hand = self.cur_color_order[:2]
        on_coming = self.cur_color_order[2:]

        if desired_combo == '蓝白红':
            combo = ['blue', 'white', 'red']
        elif desired_combo == '红白绿':
            combo = ['red', 'white', 'green']

        if len(set(on_hand).intersection(set(combo))) == 2:

            return 'Already on hand'

    def handler_desired(self, desired_combo):
        for combo in self.dict_combos:
            if combo['combo'] == desired_combo:
                txt = self.determine_consuming_order(desired_combo)
                combo['btn'].config(state=tk.DISABLED)
                combo['lbl'].config(text=txt, fg='black')
            else:
                combo['btn'].config(state=tk.NORMAL)
                combo['lbl'].config(text='')

    def handler_consume(self, pos):
        self.prev_color_order = self.cur_color_order[:]
        on_hand = self.cur_color_order[:2]
        on_coming = self.cur_color_order[2:]

        next_weapon = on_coming.pop(0)
        on_coming.append(on_hand[pos])
        on_hand[pos] = next_weapon
        self.cur_color_order = on_hand + on_coming
        self.config_btns()

    def handler_reset(self):
        self.cur_color_order = self.init_color_order[:]
        self.config_btns()
        for combo in self.dict_combos:
            combo['btn'].config(state=tk.NORMAL)
            combo['lbl'].config(text='')

    def handler_undo(self):
        self.cur_color_order = self.prev_color_order[:]
        self.config_btns()

    def handler_set_order(self):
        window_set_order = tk.Toplevel(self.window)
        window_set_order.title("Set Weapon Order")
        frm_set_order = tk.Frame(master=window_set_order)
        frm_set_order.pack()

        for i, color in enumerate(self.cur_color_order):
            button = tk.Button(master=frm_set_order,
                               text=self.get_weapon_by_color(color).name,
                               fg=color,
                               font=("Open Sans", 20),
                               image=self.get_weapon_by_color(color).img,
                               height=320,
                               width=280,
                               )
            button.grid(row=0, column=i)
            button.config(command=lambda b=button, c=color: self.handler_select_weapon(b, c))

        tk.Button(master=frm_set_order, text="Confirm", font=('Open Sans', 20),
                  command=lambda: self.handler_confirm_order(window_set_order)).grid(row=1, column=0, columnspan=5)

    def handler_select_weapon(self, btn, color):
        self.selected_order.append(color)
        btn.config(state=tk.DISABLED,
                   relief=tk.SUNKEN,
                   text=f"Selected ({len(self.selected_order)})",
                   fg="black",
                   compound=tk.BOTTOM,
                   font=('Open Sans', 20))

    def handler_confirm_order(self, window_set_order):
        if len(self.selected_order) != 5:
            return
        self.cur_color_order = self.selected_order[:]
        self.config_btns()
        self.selected_order.clear()
        window_set_order.destroy()

    def config_btns(self):
        for i, color in enumerate(self.cur_color_order):
            self.btns_weapon[i].config(text=self.get_weapon_by_color(color).name, fg=color, image=self.get_weapon_by_color(color).img)

    def get_weapon_by_color(self, color):
        if color == "green":
            return self.calibrum
        elif color == "red":
            return self.severum
        elif color == "purple":
            return self.gravitium
        elif color == "blue":
            return self.infernum
        elif color == "white":
            return self.crescendum

    def run(self):
        self.window.mainloop()


class Weapon:
    def __init__(self, name_en, name_zh, img, color):
        self.color = color
        self.img = ImageTk.PhotoImage(Image.open(img))
        if app_lang == 'zh':
            self.name = name_zh
        else:
            self.name = name_en


if __name__ == '__main__':
    gui = WeaponsRotationSimulator()
    gui.run()
