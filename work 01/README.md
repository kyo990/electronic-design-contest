# work1：Wokwi 点亮 RGB 灯

> 学习步骤、每关填空骨架和排错表见 **[`闯关指南.md`](闯关指南.md)**。

本目录对应课程发布的《Wokwi 点亮 RGB 灯训练任务书》，截止日期 **2026-11-17**。

> 任务书 PDF 不随公开仓库分发，请从课程平台获取。

## 任务要求

- 平台：Wokwi 在线仿真（wokwi.com）
- 开发板：Raspberry Pi Pico
- 语言：MicroPython
- RGB 灯：共阴（公共端接 GND，高电平点亮）
- 引脚：GP10、GP11、GP12 初始化为输出，每个颜色脚串一个限流电阻
- 效果循环：
  1. 红、绿、蓝依次单独亮，每次 1 秒；
  2. 全亮（白光）1 秒、全灭 1 秒，交替闪烁；
  3. 红+绿、绿+蓝、蓝+红两两组合，依次显示黄、青、紫，每色 1 秒。
- 代码约束：最大缩进不超过两层；全亮/全灭必须对三个引脚统一操作，不许抄三遍赋值。

## 接线表

| RGB 灯引脚 | 连接 | Pico 引脚 |
|---|---|---|
| COM（公共端） | 直接接 GND（黑线） | `pico:GND.1` |
| R（红） | 串 220Ω 电阻 | `pico:GP10` |
| G（绿） | 串 220Ω 电阻 | `pico:GP11` |
| B（蓝） | 串 220Ω 电阻 | `pico:GP12` |

Wokwi 元件类型：

- Pico：`wokwi-pi-pico`
- RGB 灯：`wokwi-rgb-led`，**默认共阳**，必须在 `attrs` 中设 `"common": "cathode"`
- 电阻：`wokwi-resistor`，`"attrs": {"value": "220"}`

### 实测颜色映射（待填写）

接线完成后，记录元件 R/G/B 脚实际对应的 Pico 引脚：

| 元件脚 | 实际接的 Pico 引脚 | 代码中的顺序 |
|---|---|---|
| R |  |  |
| G |  |  |
| B |  |  |

## 运行方式

### 方式一：Wokwi 在线版

1. 打开 <https://wokwi.com/>，登录后新建 Raspberry Pi Pico + MicroPython 工程。
2. 在 `diagram.json` 对应的图形界面中摆元件、接线。
3. 把 `main.py` 粘贴到在线编辑器中，点击运行。
4. 在线验证通过后，把 `main.py` 和 `diagram.json` 同步回本目录。

### 方式二：VS Code + Wokwi 插件

1. 用 VS Code 打开 `d:\EC\work 01` 作为工作区。
2. 安装 **Wokwi for VS Code** 扩展，申请免费 license。
3. 下载 Pico MicroPython 固件，放到 `firmware/` 目录（固件不入库）。
4. 确认 `wokwi.toml` 中的文件名与实际固件一致。
5. 在命令面板执行 **Wokwi: Start Simulator**。
6. 另开终端运行：

   ```bash
   python -m mpremote connect port:rfc2217://localhost:4000 run main.py
   ```

注意：仿真标签页必须保持可见，否则 Wokwi 会暂停，`mpremote` 会超时。

### 固件版本

- 文件：`RPI_PICO-20260824-v1.29.0.uf2`
- 来源：<https://github.com/wokwi/wokwi-vscode-micropython/tree/main/pi-pico>
- 说明：二进制固件不提交到 git；换版本时同步修改 `wokwi.toml`。

## 本目录文件

| 文件 | 说明 |
|---|---|
| `闯关指南.md` | 六关学习路径、填空骨架、验收点、排错表 |
| `main.py` | MicroPython 程序（起点模板，按关卡逐步替换） |
| `diagram.json` | 电路连线（已按共阴 RGB + GP10/11/12 配置） |
| `wokwi.toml` | VS Code 仿真配置 |
| `README.md` | 任务、接线、运行方式 |
| `NOTES.md` | 学习记录、排错记录、总结 |
| `firmware/` | Pico MicroPython 固件（不入库） |

## 验收清单

- [ ] COM 接 GND，R/G/B 各串 220Ω 后接 GP10/GP11/GP12
- [ ] `diagram.json` 中 RGB 灯为共阴（`"common": "cathode"`）
- [ ] 上电自动运行，不需要按键
- [ ] 效果一：红、绿、蓝依次单独亮，各 1 秒
- [ ] 效果二：全亮 1 秒、全灭 1 秒交替
- [ ] 效果三：黄、青、紫依次各 1 秒
- [ ] 三个效果循环播放，颜色顺序正确，无乱闪/鬼影
- [ ] 全亮/全灭为通用循环写法，没有三行重复赋值
- [ ] 最大缩进不超过两层
- [ ] 修改 `DELAY` 后闪烁速度确实变化
- [ ] `NOTES.md` 含接错次数、排查过程、0.05 秒实验结论
- [ ] VS Code 仿真可运行，现象与在线版一致
- [ ] 固件未入库

## 开源许可

本项目采用 [MIT License](../LICENSE)。
