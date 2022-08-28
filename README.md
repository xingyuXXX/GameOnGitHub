# GAMES

by **XingyuZhou**

---

⚠️ ：目前只适用于官匹 64 tick；

- [GAMES](#games)
  - [CSGO](#csgo)
    - [电脑设置](#电脑设置)
    - [启动项](#启动项)
    - [实用指令](#实用指令)
    - [键位代码](#键位代码)
  - [LOL](#lol)

## CSGO

### 电脑设置

`Win R | control` 进入控制中心：

1. `鼠标 | 指针选项 | 取消 提高指针精确度`
2. `轻松使用设置中心 | 使鼠标更易使用 | 设置鼠标键 | 最高速度/加速 全拉最低`
3. `键盘 | 速度 | 重复延迟/重复速度 调到 短/快`

> 鼠标 DPI: 800-1000

### 启动项

位置：`Steam | 库 | CSGO | 属性 | 启动项`；

```text
-high -novid -nojoy +exec main_xy.cfg -fullscreen -allow_third_party_software
```

- `-high`：提高 CSGO 优先级；
- `-novid`：关闭过场动画；
- `-nojoy`：不使用摇杆，可提高少部分性能；
- `+exec main_xy.cfg`：执行自己的配置文件；
- `-fullscreen`：全屏；
- `-allow_third_party_software` (optional): 允许使用微星小飞机监控；

### 实用指令

输出当前准星参数：

```text
echo ;echo "=== 准星参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text cl_crosshair;host_writeconfig;con_filter_text cl_fix;host_writeconfig;developer 0;con_filter_enable 0;
```

输出当前持枪参数：

```text
echo ;echo "=== 持枪参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text viewmodel;host_writeconfig;con_filter_text cl_bob;host_writeconfig;developer 0;con_filter_enable 0;
```

### 键位代码

鼠标键区：

|  键位  |   code   |   键位   |     code     |
| :----: | :------: | :------: | :----------: |
|  左键  | `mouse1` |  前侧键  |   `mouse5`   |
|  右键  | `mouse2` | 滚轮上滑 |  `mwheelup`  |
|  中键  | `mouse3` | 滚轮下滑 | `mwheeldown` |
| 后侧键 | `mouse4` |          |              |

主键区：

| 键位  |   code    |
| :---: | :-------: |
| 0 ~ 9 | `0` ~ `9` |
| a ~ z | `a` ~ `z` |
| 空格  |  `space`  |

符号键区：

| 键位  | code  | 键位  |    code     |
| :---: | :---: | :---: | :---------: |
|   -   |  `-`  |   \   |     `\`     |
|   =   |  `=`  |   ;   | `semicolon` |
|   [   |  `[`  |   '   |     `'`     |
|   ]   |  `]`  |   .   |     `.`     |
|   /   |  `/`  |       |             |

控制键区：

|    键位    |    code     |      键位      |       code       |
| :--------: | :---------: | :------------: | :--------------: |
|   退格键   | `backspace` | 左/右 Shift 键 | `shift`/`rshift` |
|  制表符键  |    `tab`    | 左/右 Ctrl 键  |  `ctrl`/`rctrl`  |
|   回车键   |   `enter`   |  左/右 Alt 键  |   `alt`/`ralt`   |
| 大写锁定键 | `capslock`  |                |                  |

编辑键区：

|           键位           |                      code                      |
| :----------------------: | :--------------------------------------------: |
|          Insert          |                     `ins`                      |
|          Delete          |                     `del`                      |
|           Home           |                     `home`                     |
|           End            |                     `end`                      |
|     PageUp/PageDown      |                 `pgup`/`pgdn`                  |
| Up/Down/Left/Right Arrow | `uparrow`/`downarrow`/`leftarrow`/`rightarrow` |

功能键区：

|   键位   |     code     |
| :------: | :----------: |
| F1 ~ F12 | `f1` ~ `f12` |

小键盘区：

|   键位   |      code       |     键位     |     code      |
| :------: | :-------------: | :----------: | :-----------: |
| 小键盘 1 |    `kp_end`     |   小键盘 9   |   `kp_pgup`   |
| 小键盘 2 | `kp_downarrow`  |   小键盘 0   |   `kp_ins`    |
| 小键盘 3 |    `kp_pgdn`    |   小键盘 .   |   `kp_del`    |
| 小键盘 4 | `kp_leftarrow`  |   小键盘 /   |  `kp_slash`   |
| 小键盘 5 |     `kp_5`      |   小键盘 *   | `kp_multiply` |
| 小键盘 6 | `kp_rightarrow` |   小键盘 -   |  `kp_minus`   |
| 小键盘 7 |    `kp_home`    |   小键盘 +   |   `kp_plus`   |
| 小键盘 8 |  `kp_uparrow`   | 小键盘 Enter |  `kp_enter`   |

## LOL

OPTIONS:

- HOTKEYS:
  1. ✅ Cast the pressed spell upon pressing another spell
  2. Level Up Spell 4: `MB4`
  3. Target Champions Only: `MB5`

- INTERFACE:
  - Interface Size
    1. HUD Scale: `0`
    2. Cursor Scale: `36`
    3. Minimap Scale: `66`
  - Notifications
    1. ❎ Screen flash on damage
    2. ❎ Screen flash on loss of control
  - Ability and Attack Display
    1. ✅ Show Spell costs
    2. Ability Cooldown Display: `Minutes + Seconds`
  - Minimap
    1. ❎ Allow Minimap movement
  - Scoreboard:
    1. ✅ Show Summoner names

- GAME:
  - Controls
    1. Mouse Speed: `40`
    2. Camera Move Speed (Mouse): `28`
    3. Camera Move Speed (Keyboard): `0`
    > 鼠标 DPI: 800-1000
  - Gameplay
    1. ❎ Use movement prediction
    2. ✅ Attack move on cursor
    3. ✅ Treat 'Target Champions Only' as a toggle