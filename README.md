# CSGOonGit

by **XingyuZhou**

---

⚠️ ：目前只适用于官匹 64 tick；

## 电脑设置

`Win R | control` 进入控制中心：

1. `鼠标 | 指针选项 | 取消 提高指针精确度`
2. `轻松使用设置中心 | 使鼠标更易使用 | 设置鼠标键 | 最高速度/加速 全拉最低`
3. `键盘 | 速度 | 重复延迟/重复速度 调到 短/快`

## 启动项

位置：`Steam | 库 | CSGO | 属性 | 启动项`；

```text
-high -novid -nojoy -refresh 80 -preload +exec main_xy.cfg -w 1280 -h 960 -fullscreen
```

- `-high`：提高 CSGO 优先级；
- `-novid`：关闭过场动画；
- `-nojoy`：不使用摇杆，可提高少部分性能；
- `-refresh 80`：设置刷新率为 80，根据显示器调整；
- `-preload`：预加载纹理和建模，可以提高性能；
- `+exec main_xy.cfg`：执行自己的配置文件；
- `-w 1280 -h 960`：设置分辨率为 1280*960；
- `-fullscreen`：全屏；

## 实用指令

自用准星代码：

```text
CSGO-PcVAb-Dinja-VQrf3-rNtwt-9zN6H
```

输出当前准星参数：

```text
echo ;echo "=== 准星参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text cl_crosshair;host_writeconfig;con_filter_text cl_fix;host_writeconfig;developer 0;con_filter_enable 0;
```

输出当前持枪参数：

```text
echo ;echo "=== 持枪参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text viewmodel;host_writeconfig;con_filter_text cl_bob;host_writeconfig;developer 0;con_filter_enable 0;
```
