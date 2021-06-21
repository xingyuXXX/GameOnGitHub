# CSGOonGit

by **XingyuZhou**

---

## 启动项

位置：`Steam | 库 | CSGO 属性 | 启动项`；

```text
-high -novid -nojoy -refresh 80 -preload +exec xingyu.cfg -w 1280 -h 960 -fullscreen
```

- `-high`：提高 CSGO 优先级；
- `-novid`：关闭过场动画；
- `-nojoy`：不使用摇杆，可提高少部分性能；
- `-refresh 80`：设置刷新率为 80，根据显示器调整；
- `-preload`：预加载纹理和建模，可以提高性能；
- `+exec xingyu.cfg`：执行自己的配置文件；
- `-w 1280 -h 960`：设置分辨率1280*960；
- `-fullscreen`：全屏；

## 实用指令

输出当前准星参数：

```text
echo ;echo "=== 准星参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text cl_crosshair;host_writeconfig;con_filter_text cl_fix;host_writeconfig;developer 0;con_filter_enable 0;
```

输出当前持枪参数：

```text
echo ;echo "=== 持枪参数 ===";echo ;developer 2;con_filter_enable 1;con_filter_text viewmodel;host_writeconfig;con_filter_text cl_bob;host_writeconfig;developer 0;con_filter_enable 0;
```
