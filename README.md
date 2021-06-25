# CSGOonGit

by **XingyuZhou**

---

⚠️ ：目前只适用于官匹 64 tick；

## 电脑设置

`Win R | control` 进入控制中心：

1. `鼠标 | 指针选项 | 取消 提高指针精确度`
2. `轻松使用设置中心 | 使鼠标更易使用 | 设置鼠标键 | 最高速度/加速 全拉最低`
3. `键盘 | 速度 | 重复延迟/重复速度 调到 短/快`

进入 Nvidia 控制面板：

1. 管理 3D 设置：
   - `程序设置 | 选择 CSGO`；
   - `为此程序选择首选图形处理器 | 高性能 Nvidia 处理器`；
   - `指定该程序的设置值`：
 
| 功能 | 设置 |
|:----:|:---:|
| CUDA - GPUs | 全部 |
| OpenGL 渲染 GPU | 自动选择 |
| 三重缓冲 | 关 |
| 各向异性过滤 | 关 |
| 垂直同步 | 关 |
| 平滑处理 - 模式 | 关 |
| 平滑处理 - 灰度纠正 | 关 |
| 最大预渲染帧数 | 1 |
| 环境光吸收 | 关 |
| 电池管理模式 | 最高性能优先 |
| 着色缓冲器 | 开 |
| 纹理过滤 - 三线性优化 | 开 |
| 纹理过滤 - 各向异性采样优化 | 开 |
| 纹理过滤 - 负 LOD 偏移 | 允许 |
| 纹理过滤 - 质量 | 高性能 |
| 线程优化 | 自动 |
| 虚拟现实预渲染帧数 | 1 |

> 各选项下面都有提示，依据性能优先的原则选择；

2. 通过预览调整图像设置：
   - `使用我的优先选择：侧重于性能`

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
