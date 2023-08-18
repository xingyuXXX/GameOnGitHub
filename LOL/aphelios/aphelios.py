import os.path
import random
import sys
import tkinter as tk
from PIL import ImageTk, Image

app_lang = 'zh'


def get_resource_path(img_file):
    relative_path = os.path.join('weapons', img_file)
    if hasattr(sys, '_MEIPASS'):    # for PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


class WeaponsRotationSimulator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aphelios Weapons Rotaion Simulator")

        self.frm_weapons = tk.Frame()
        self.frm_weapons.grid(row=0, column=0)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.grid(row=1, column=0)

        self.calibrum = Weapon("Calibrum", '通碧', get_resource_path('Calibrum.png'), "green")
        self.severum = Weapon("Severum", '断魄', get_resource_path('Severum.png'), "red")
        self.gravitium = Weapon("Gravitium", '坠明', get_resource_path('Gravitium.png'), "purple")
        self.infernum = Weapon("Infernum", '荧焰', get_resource_path('Infernum.png'), "blue")
        self.crescendum = Weapon("Crescendum", '折镜', get_resource_path('Crescendum.png'), "white")

        self.init_color_order = ['green', 'red', 'purple', 'blue', 'white']
        self.cur_color_order = self.init_color_order[:]
        self.prev_color_order = self.init_color_order[:]
        self.seleted_order = []

        self.btns_weapon = []
        for i, wp_color in enumerate(self.init_color_order):

            if i in [0, 1]: # does not work on macOS
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
            if i == 1:
                button.grid(row=0, column=i, padx=(0, 40))
            else:
                button.grid(row=0, column=i)
            self.btns_weapon.append(button)

        tk.Button(master=self.frm_buttons, text="Reset", font=('Open Sans', 20), command=self.handler_reset).grid(row=0, column=0)
        tk.Button(master=self.frm_buttons, text="Undo", font=('Open Sans', 20), command=self.handler_undo).grid(row=0, column=1)
        tk.Button(master=self.frm_buttons, text="Set Order", font=('Open Sans', 20),
                  command=self.handler_set_order).grid(row=0, column=2, padx=(20, 0))
        self.btns_weapon[0].config(command=self.handler_main_hand)
        self.btns_weapon[1].config(command=self.handler_off_hand)

    def handler_main_hand(self):
        self.consume_weapon(self.get_weapon_by_color(self.cur_color_order[0]))
        self.config_btns()

    def handler_off_hand(self):
        self.consume_weapon(self.get_weapon_by_color(self.cur_color_order[1]))
        self.config_btns()

    def handler_reset(self):
        self.cur_color_order = self.init_color_order[:]
        self.config_btns()

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
        self.seleted_order.append(color)
        btn.config(state=tk.DISABLED,
                   relief=tk.SUNKEN,
                   text=f"Selected ({len(self.seleted_order)})",
                   fg="black",
                   compound=tk.BOTTOM,
                   font=('Open Sans', 20))

    def handler_confirm_order(self, window_set_order):
        if len(self.seleted_order) != 5:
            return
        self.cur_color_order = self.seleted_order[:]
        self.config_btns()
        self.seleted_order.clear()
        window_set_order.destroy()

    def consume_weapon(self, weapon):
        self.prev_color_order = self.cur_color_order[:]
        self.cur_color_order.remove(weapon.color)
        self.cur_color_order.append(weapon.color)

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
