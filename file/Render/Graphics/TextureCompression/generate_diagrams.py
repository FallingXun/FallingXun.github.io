from pathlib import Path
from html import escape as esc

OUT = Path(r"D:\My\Git\UnityAstcGpuEncoder\docs\texture-compression\images")
OUT.mkdir(parents=True, exist_ok=True)

BG = "#ffffff"
INK = "#172033"
MUTED = "#64748b"
LINE = "#cbd5e1"
SOFT = "#f8fafc"
BLUE = "#2563eb"
TEAL = "#0f766e"
ORANGE = "#ea580c"
PURPLE = "#7c3aed"
ROSE = "#e11d48"
AMBER = "#d97706"
GREEN = "#16a34a"
FONT = "Microsoft YaHei, Noto Sans CJK SC, Segoe UI, Arial, sans-serif"
MONO = "Cascadia Mono, Consolas, monospace"


def text(x, y, s, size=18, fill=INK, weight=400, anchor="start", mono=False, opacity=1):
    family = MONO if mono else FONT
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{family}" text-anchor="{anchor}" opacity="{opacity}">{esc(s)}</text>')


def lines(x, y, items, size=17, fill=INK, leading=24, weight=400, mono=False):
    out = [f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" font-family="{MONO if mono else FONT}">']
    for i, item in enumerate(items):
        dy = 0 if i == 0 else leading
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(item)}</tspan>')
    out.append('</text>')
    return "".join(out)


def rect(x, y, w, h, fill=SOFT, stroke=LINE, rx=12, sw=1.5, dash=None, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{d}/>')


def line(x1, y1, x2, y2, stroke=LINE, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow(x1, y1, x2, y2, stroke=MUTED, sw=2.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" '
            f'marker-end="url(#arrow)"{d}/>')


def circle(cx, cy, r, fill, stroke="none", sw=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def svg(w, h, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="{BG}"/>
{body}
</svg>
'''


def save(name, w, h, title, body):
    (OUT / name).write_text(svg(w, h, title, body), encoding="utf-8")


def grid(x, y, cell, cols, rows, colors, gap=2, rx=3):
    out = []
    for r in range(rows):
        for c in range(cols):
            out.append(rect(x + c * cell, y + r * cell, cell - gap, cell - gap,
                            colors[(r * cols + c) % len(colors)], "none", rx))
    return "".join(out)


def badge(x, y, label, color, width=None, size=15):
    w = width or (len(label) * size * 0.7 + 28)
    return (rect(x, y, w, 32, color + "18", color, 16, 1.2) +
            text(x + w / 2, y + 22, label, size, color, 600, "middle"))


# ---------------------------------------------------------------------------
# 01 overview
# ---------------------------------------------------------------------------
b = []
b.append(text(60, 64, "纹理压缩：用固定大小的块表示大量像素", 32, INK, 700))
b.append(text(60, 98, "块压缩把图像切成小块，每块独立编码、独立解码，适合 GPU 的随机访问。", 18, MUTED))

b.append(rect(55, 130, 320, 410, "#f8fafc", "#dbe4ee", 20))
b.append(text(80, 168, "原始纹理", 20, INK, 700))
b.append(text(80, 194, "8 × 8 texel（示例）", 15, MUTED))
palette = ["#fecaca", "#fed7aa", "#fef08a", "#bbf7d0", "#bfdbfe", "#ddd6fe", "#fbcfe8", "#c7d2fe"]
b.append(grid(110, 235, 30, 8, 8, palette, 3, 4))
b.append(text(270, 505, "相邻像素有空间相关性", 14, MUTED, 400, "middle"))
b.append(text(270, 526, "可利用端点 + 权重近似表示", 14, MUTED, 400, "middle"))

b.append(arrow(390, 340, 505, 340))
b.append(text(448, 320, "按块编码", 15, MUTED, 600, "middle"))

b.append(rect(520, 150, 300, 370, "#0f172a", "#0f172a", 20))
b.append(text(545, 190, "一个压缩块", 21, "#f8fafc", 700))
b.append(text(545, 218, "ASTC：固定 128 bit = 16 bytes", 15, "#a7b4c8"))
b.append(rect(548, 250, 244, 50, "#172b4d", "#365a8c", 9))
b.append(text(565, 283, "Block Mode", 16, "#93c5fd", 600))
b.append(text(775, 283, "11 bit", 15, "#dbeafe", 500, "end", True))
b.append(rect(548, 312, 244, 50, "#173f3b", "#2d7066", 9))
b.append(text(565, 345, "Endpoints", 16, "#99f6e4", 600))
b.append(text(775, 345, "2 × RGB", 15, "#ccfbf1", 500, "end", True))
b.append(rect(548, 374, 244, 50, "#3b2a56", "#7c5aa6", 9))
b.append(text(565, 407, "Weights / Grid", 16, "#ddd6fe", 600))
b.append(text(775, 407, "2–6 bit", 15, "#ede9fe", 500, "end", True))
b.append(rect(548, 436, 244, 50, "#4a2b16", "#9a5b25", 9))
b.append(text(565, 469, "Partition / Flags", 16, "#fed7aa", 600))
b.append(text(775, 469, "按模式解释", 15, "#ffedd5", 500, "end"))
b.append(text(670, 510, "解码端只读当前块，不需要其他块", 13, "#a7b4c8", 400, "middle"))

b.append(arrow(850, 340, 965, 340))
b.append(text(907, 320, "硬件解码", 15, MUTED, 600, "middle"))

b.append(rect(980, 130, 165, 410, "#f8fafc", "#dbe4ee", 20))
b.append(text(1003, 168, "解码结果", 20, INK, 700))
b.append(text(1003, 194, "逐 texel 颜色", 15, MUTED))
b.append(grid(1000, 235, 18, 8, 8, ["#fecaca", "#fed7aa", "#fef08a", "#bbf7d0", "#bfdbfe", "#ddd6fe", "#fbcfe8", "#c7d2fe"], 2, 3))
b.append(text(1062, 505, "再进入过滤/采样", 13, MUTED, 400, "middle"))

b.append(rect(60, 570, 320, 52, "#eff6ff", "#bfdbfe", 14))
b.append(text(220, 602, "固定码率：每块字节数固定", 16, "#1d4ed8", 600, "middle"))
b.append(rect(445, 570, 320, 52, "#ecfdf5", "#a7f3d0", 14))
b.append(text(605, 602, "随机访问：不依赖其他块", 16, "#047857", 600, "middle"))
b.append(rect(830, 570, 310, 52, "#fff7ed", "#fed7aa", 14))
b.append(text(985, 602, "近似压缩：解码不是原图", 16, "#c2410c", 600, "middle"))
save("01-overview.svg", 1200, 650, "纹理压缩概览", "".join(b))

# ---------------------------------------------------------------------------
# 02 astc pipeline
# ---------------------------------------------------------------------------
b = []
b.append(text(55, 60, "ASTC：从一个块到 128 bit 码流", 32, INK, 700))
b.append(text(55, 94, "ASTC 没有唯一固定的块布局；Block Mode 决定分区、端点模式、权重网格和权重位宽。", 18, MUTED))

# source block
b.append(rect(45, 135, 195, 225, "#f8fafc", "#dbe4ee", 16))
b.append(text(65, 170, "① 源块", 19, INK, 700))
colors = ["#fca5a5", "#fdba74", "#fde68a", "#86efac", "#93c5fd", "#c4b5fd", "#f9a8d4", "#a5f3fc"]
b.append(grid(68, 195, 23, 6, 6, colors, 3, 4))
b.append(text(142, 345, "6 × 6 texel", 14, MUTED, 400, "middle"))

b.append(arrow(245, 245, 285, 245))
# partition
b.append(rect(292, 135, 200, 225, "#f8fafc", "#dbe4ee", 16))
b.append(text(312, 170, "② 分区", 19, INK, 700))
b.append(text(312, 196, "1–4 个 partition", 14, MUTED))
# partition schematic
b.append(rect(320, 220, 144, 82, "#dbeafe", "#93c5fd", 8))
b.append(rect(320, 220, 70, 82, "#fed7aa", "#fdba74", 8))
b.append(text(355, 267, "P0", 19, BLUE, 700, "middle"))
b.append(text(390, 267, "P1", 19, ORANGE, 700, "middle"))
b.append(lines(392, 324, ["同块内不同区域", "可用不同端点"], 12, MUTED, 16, 400))

b.append(arrow(497, 245, 537, 245))
# endpoints
b.append(rect(544, 135, 205, 225, "#f8fafc", "#dbe4ee", 16))
b.append(text(564, 170, "③ 端点", 19, INK, 700))
b.append(text(564, 196, "每个分区 2 个端点", 14, MUTED))
b.append(circle(595, 265, 20, "#93c5fd", "#2563eb", 2))
b.append(circle(695, 265, 20, "#fca5a5", "#e11d48", 2))
b.append(line(615, 265, 675, 265, "#94a3b8", 3))
b.append(text(595, 305, "Min", 13, BLUE, 600, "middle"))
b.append(text(695, 305, "Max", 13, ROSE, 600, "middle"))
b.append(text(646, 335, "color = Min + t × (Max − Min)", 13, MUTED, 400, "middle", True))

b.append(arrow(754, 245, 794, 245))
# weights
b.append(rect(801, 135, 205, 225, "#f8fafc", "#dbe4ee", 16))
b.append(text(821, 170, "④ 权重", 19, INK, 700))
b.append(text(821, 196, "投影到 Min→Max 上", 14, MUTED))
# small 4x4 weight grid
for r in range(4):
    for c in range(4):
        v = (r * 4 + c) % 8
        col = "#dbeafe" if v < 4 else "#bfdbfe"
        b.append(rect(840 + c * 24, 225 + r * 24, 20, 20, col, "#93c5fd", 4))
        b.append(text(850 + c * 24, 240 + r * 24, str(v), 11, BLUE, 600, "middle", True))
b.append(text(903, 335, "量化成 2–6 bit / 值", 13, MUTED, 400, "middle"))

b.append(arrow(1011, 245, 1051, 245))
# pack
b.append(rect(1058, 135, 100, 225, "#0f172a", "#0f172a", 16))
b.append(text(1108, 170, "⑤ 打包", 18, "#f8fafc", 700, "middle"))
b.append(text(1108, 214, "128", 34, "#93c5fd", 700, "middle", True))
b.append(text(1108, 242, "bit", 15, "#a7b4c8", 600, "middle"))
b.append(text(1108, 300, "16 B", 17, "#99f6e4", 700, "middle", True))
b.append(text(1108, 326, "每块", 12, "#a7b4c8", 400, "middle"))

# bitstream
b.append(rect(55, 425, 1090, 135, "#f8fafc", "#dbe4ee", 16))
b.append(text(78, 460, "ASTC 块的通用逻辑结构", 18, INK, 700))
b.append(text(78, 485, "具体字段数量和排列由 Block Mode 决定；下图表示解码器需要理解的语义，而不是唯一的物理布局。", 14, MUTED))
fields = [
    (78, 515, 180, "#dbeafe", BLUE, "Block Mode", "尺寸/分区/网格"),
    (270, 515, 300, "#ede9fe", PURPLE, "配置与分区", "partition / plane"),
    (582, 515, 260, "#ccfbf1", TEAL, "端点", "量化颜色"),
    (854, 515, 270, "#ffedd5", ORANGE, "权重网格", "2–6 bit / 值"),
]
for x, y, w, fill, color, title, sub in fields:
    b.append(rect(x, y, w, 26, fill, color, 6))
    b.append(text(x + 10, y + 18, title, 12, color, 700))
    b.append(text(x + w - 10, y + 18, sub, 10, color, 500, "end"))

b.append(rect(55, 590, 1090, 72, "#eff6ff", "#bfdbfe", 14))
b.append(text(80, 621, "解码公式", 15, "#1d4ed8", 700))
b.append(text(185, 621, "color(texel) = Endpoint0 + w(texel) / (2ⁿ−1) × (Endpoint1 − Endpoint0)", 17, "#1e3a8a", 500, True))
b.append(text(80, 646, "其中 w(texel) 由权重网格按位置双线性插值得到；n 是每个权重值的位数。", 13, "#475569"))
save("02-astc-pipeline.svg", 1200, 700, "ASTC 编码与解码流程", "".join(b))

# ---------------------------------------------------------------------------
# 03 block sizes
# ---------------------------------------------------------------------------
b = []
b.append(text(55, 60, "ASTC 的块尺寸：质量、码率与空间的取舍", 32, INK, 700))
b.append(text(55, 94, "所有 ASTC 块都固定为 128 bit；改变块覆盖的 texel 数，就改变了比特率。", 18, MUTED))

cards = [
    ("4 × 4", 4, "16 texel", "8.00 bpp", "高质量", "#dbeafe", BLUE),
    ("5 × 5", 5, "25 texel", "5.12 bpp", "均衡", "#ccfbf1", TEAL),
    ("6 × 6", 6, "36 texel", "3.56 bpp", "更省内存", "#ede9fe", PURPLE),
    ("8 × 8", 8, "64 texel", "2.00 bpp", "明显压缩", "#ffedd5", ORANGE),
    ("12 × 12", 12, "144 texel", "0.89 bpp", "极致省内存", "#ffe4e6", ROSE),
]
x0 = 55
for i, (name, n, texels, bpp, quality, fill, color) in enumerate(cards):
    x = x0 + i * 224
    b.append(rect(x, 135, 202, 335, fill + "55", color, 18, 1.6))
    b.append(text(x + 18, 173, name, 23, color, 700))
    b.append(text(x + 18, 201, texels, 14, MUTED))
    # block grid
    gx, gy, gs = x + 28, 225, 146
    cols = n
    cell = gs / cols
    for r in range(cols):
        for c in range(cols):
            shade = "#ffffff" if (r + c) % 2 == 0 else fill
            b.append(rect(gx + c * cell + 1, gy + r * cell + 1, max(1, cell - 2), max(1, cell - 2), shade, color, 2, 0.8))
    b.append(text(x + 101, 397, bpp, 25, color, 700, "middle", True))
    b.append(text(x + 101, 424, quality, 15, MUTED, 600, "middle"))
    b.append(text(x + 101, 449, "128 bit / block", 12, color, 500, "middle", True))

b.append(rect(55, 510, 1090, 130, "#f8fafc", "#dbe4ee", 16))
b.append(text(78, 545, "比特率怎么算？", 18, INK, 700))
b.append(text(78, 577, "bpp = 128 bit / (blockWidth × blockHeight)", 18, BLUE, 600, "start", True))
b.append(text(78, 609, "块越大，每 texel 分到的位数越少：4×4 = 8 bpp，12×12 ≈ 0.89 bpp。", 14, MUTED))
b.append(text(78, 630, "大块适合低频、缓变的表面；细节、文字、边缘和高频法线通常要选更小的块。", 14, MUTED))

b.append(rect(600, 535, 515, 84, "#fff7ed", "#fed7aa", 12))
b.append(text(620, 565, "注意：bpp 不是唯一指标", 15, "#c2410c", 700))
b.append(text(620, 590, "块越大，编码器越难用一条渐变拟合块内细节；", 13, "#7c2d12"))
b.append(text(620, 610, "通常需要分区、双平面或更多搜索来弥补质量。", 13, "#7c2d12"))
save("03-block-sizes.svg", 1200, 680, "ASTC 块尺寸与比特率", "".join(b))

# ---------------------------------------------------------------------------
# 04 weight grid
# ---------------------------------------------------------------------------
b = []
b.append(text(55, 60, "权重网格：从粗网格插值到每个 texel", 32, INK, 700))
b.append(text(55, 94, "大块不会为每个 texel 存一个权重，而是存一张更小的权重网格，解码时双线性上采样。", 18, MUTED))

# left 8x8 texel grid with 4x4 grid points
b.append(rect(55, 135, 475, 465, "#f8fafc", "#dbe4ee", 18))
b.append(text(78, 172, "8 × 8 块 + 4 × 4 权重网格", 20, INK, 700))
b.append(text(78, 198, "每个网格点覆盖一个 2 × 2 texel 单元", 14, MUTED))
cell = 38
gx, gy = 132, 235
for r in range(8):
    for c in range(8):
        b.append(rect(gx + c * cell, gy + r * cell, cell - 2, cell - 2, "#ffffff", "#cbd5e1", 2, 1))
for r in range(4):
    for c in range(4):
        cx = gx + c * 2 * cell + cell
        cy = gy + r * 2 * cell + cell
        b.append(circle(cx, cy, 8, BLUE, "#ffffff", 2))
        b.append(text(cx + 12, cy + 5, f"G{r}{c}", 10, BLUE, 700, "start", True))
# highlight one texel and neighborhood
b.append(rect(gx + 3 * cell + 3, gy + 3 * cell + 3, cell - 8, cell - 8, "#f59e0b", "#b45309", 3, 3))
b.append(text(gx + 3 * cell + cell / 2, gy + 3 * cell - 8, "texel (3,3)", 11, AMBER, 700, "middle"))
b.append(text(292, 565, "● = 一个网格权重    □ = 一个 texel", 13, MUTED, 400, "middle"))

# right formula
b.append(rect(565, 135, 580, 465, "#ffffff", "#dbe4ee", 18))
b.append(text(592, 175, "双线性插值示例", 21, INK, 700))
b.append(text(592, 202, "texel (3,3) 落在网格坐标 (1.25, 1.25)", 14, MUTED))
# 2x2 grid visual
for r in range(2):
    for c in range(2):
        b.append(circle(670 + c * 150, 285 + r * 130, 14, "#bfdbfe", BLUE, 2))
        b.append(text(670 + c * 150, 291 + r * 130, f"G{1+r}{1+c}", 11, BLUE, 700, "middle", True))
b.append(rect(648, 245, 44, 20, "#fef3c7", "#f59e0b", 4, 1))
b.append(text(670, 260, "0.75", 10, AMBER, 700, "middle", True))
b.append(rect(798, 245, 44, 20, "#fef3c7", "#f59e0b", 4, 1))
b.append(text(820, 260, "0.25", 10, AMBER, 700, "middle", True))
b.append(rect(648, 375, 44, 20, "#fef3c7", "#f59e0b", 4, 1))
b.append(text(670, 390, "0.25", 10, AMBER, 700, "middle", True))
b.append(rect(798, 375, 44, 20, "#fef3c7", "#f59e0b", 4, 1))
b.append(text(820, 390, "0.75", 10, AMBER, 700, "middle", True))
b.append(text(855, 270, "x 方向", 12, MUTED, 600, "middle"))
b.append(text(608, 337, "y", 12, MUTED, 600, "middle"))
b.append(text(608, 392, "方向", 12, MUTED, 600, "middle"))

b.append(lines(592, 448, [
    "w = 0.75 × 0.75 × G11",
    "  + 0.75 × 0.25 × G12",
    "  + 0.25 × 0.75 × G21",
    "  + 0.25 × 0.25 × G22",
], 17, INK, 27, 500, True))
b.append(text(592, 575, "解码器对块内每个 texel 都做一次插值；相邻 texel 共享网格点，因此权重平滑过渡。", 13, MUTED))

b.append(rect(55, 625, 1090, 55, "#ecfdf5", "#a7f3d0", 14))
b.append(text(78, 658, "小块的网格可以等于块尺寸（每个 texel 一个权重）；大块则必须/通常把网格缩减，以把权重位放进 128 bit。", 14, "#047857", 600))
save("04-weight-grid.svg", 1200, 700, "ASTC 权重网格插值", "".join(b))

# ---------------------------------------------------------------------------
# 05 ETC
# ---------------------------------------------------------------------------
b = []
b.append(text(55, 60, "ETC：两个子块、少量基色和调制表", 32, INK, 700))
b.append(text(55, 94, "ETC1/ETC2 以固定 4×4 块为核心；ETC1 为 64 bit，ETC2 增加差分解码、T/H/Planar 和 EAC 透明通道。", 18, MUTED))

b.append(rect(55, 135, 1090, 205, "#f8fafc", "#dbe4ee", 18))
b.append(text(78, 172, "ETC1：64 bit / 4×4 块（RGB，4 bpp）", 20, INK, 700))
# subblocks
b.append(rect(88, 200, 140, 104, "#dbeafe", "#93c5fd", 8))
b.append(line(158, 200, 158, 304, "#93c5fd", 2, "5 4"))
b.append(text(158, 326, "flip：2×4 或 4×2 子块", 12, BLUE, 600, "middle"))
b.append(text(88, 358, "每个子块：基色 + table codeword + 16 个 2-bit index", 13, MUTED))
# layout fields
xs = 300
fields = [
    (300, 205, 150, "#dbeafe", BLUE, "Base Color 0", "RGB 4/4/4"),
    (470, 205, 150, "#dbeafe", BLUE, "Base Color 1", "RGB 4/4/4"),
    (640, 205, 150, "#ede9fe", PURPLE, "Modifier Table", "3 bit × 2"),
    (810, 205, 260, "#ffedd5", ORANGE, "Pixel Indices", "2 bit × 16"),
    (1085, 205, 35, "#f1f5f9", MUTED, "Flag", "2 bit"),
]
for x, y, w, fill, color, title, sub in fields:
    b.append(rect(x, y, w, 62, fill, color, 8))
    b.append(text(x + w / 2, y + 26, title, 12, color, 700, "middle"))
    b.append(text(x + w / 2, y + 46, sub, 10, MUTED, 500, "middle"))
b.append(text(1065, 296, "1 flip + 1 diff", 11, MUTED, 500, "end"))
b.append(text(1058, 317, "64 bit total", 12, BLUE, 600, "end", True))

# formula
b.append(rect(55, 370, 1090, 82, "#eff6ff", "#bfdbfe", 14))
b.append(text(78, 402, "ETC1 解码公式", 15, "#1d4ed8", 700))
b.append(text(225, 402, "color(texel) = BaseColor[subblock] + Modifier[table][index(texel)]", 18, "#1e3a8a", 500, "start", True))
b.append(text(78, 431, "每个像素只携带 2 bit 索引，因此子块内的颜色只能沿调制表给出的少量明暗台阶变化。", 13, "#475569"))

# ETC2 modes
b.append(text(55, 505, "ETC2 的扩展模式", 21, INK, 700))
mode_cards = [
    ("Individual / Differential", "子块基色独立，或第二个基色用 3-bit 有符号差值", "#dbeafe", BLUE),
    ("T 模式", "两个端点 + 一个中间色，适合双色/边缘", "#ccfbf1", TEAL),
    ("H 模式", "两个端点派生的多级明暗，适合渐变", "#ede9fe", PURPLE),
    ("Planar 模式", "用一个基色和两个斜率表示平滑平面", "#ffedd5", ORANGE),
    ("EAC 透明通道", "单独 64-bit 通道块，基值 + 倍数 + 索引", "#ffe4e6", ROSE),
]
for i, (name, desc, fill, color) in enumerate(mode_cards):
    x = 55 + (i % 3) * 365
    y = 535 + (i // 3) * 105
    w = 330 if i < 3 else 330
    b.append(rect(x, y, w, 85, fill + "66", color, 12, 1.2))
    b.append(text(x + 15, y + 27, name, 15, color, 700))
    b.append(text(x + 15, y + 52, desc, 11, MUTED))
    b.append(text(x + 15, y + 70, "64 bit", 10, color, 500, "start", True))
save("05-etc.svg", 1200, 780, "ETC 编码与解码", "".join(b))

# ---------------------------------------------------------------------------
# 06 BC
# ---------------------------------------------------------------------------
b = []
b.append(text(55, 60, "BC：桌面 GPU 的块压缩家族", 32, INK, 700))
b.append(text(55, 94, "BC 系列以固定 4×4 块为基础，颜色块通常 64 bit，RGBA/高动态范围格式使用 128 bit。", 18, MUTED))

# BC1
b.append(rect(55, 135, 520, 335, "#f8fafc", "#dbe4ee", 18))
b.append(text(78, 172, "BC1 / DXT1：64 bit，4×4，RGB 4 bpp", 19, INK, 700))
fields = [
    (78, 205, 170, "#dbeafe", BLUE, "Endpoint 0", "RGB565 · 16 bit"),
    (258, 205, 170, "#dbeafe", BLUE, "Endpoint 1", "RGB565 · 16 bit"),
    (438, 205, 108, "#ffedd5", ORANGE, "Indices", "2 bit × 16"),
]
for x, y, w, fill, color, title, sub in fields:
    b.append(rect(x, y, w, 66, fill, color, 8))
    b.append(text(x + w / 2, y + 28, title, 13, color, 700, "middle"))
    b.append(text(x + w / 2, y + 49, sub, 10, MUTED, 500, "middle"))
b.append(text(78, 310, "解码：在 E0 和 E1 之间做 2-bit 索引的线性插值。", 14, MUTED))
b.append(text(78, 342, "C0 = E0，C1 = E1", 15, BLUE, 600, "start", True))
b.append(text(78, 369, "C2 = 2/3 E0 + 1/3 E1", 15, BLUE, 600, "start", True))
b.append(text(78, 396, "C3 = 1/3 E0 + 2/3 E1", 15, BLUE, 600, "start", True))
b.append(text(78, 431, "特殊端点顺序可提供 1-bit alpha / 透明模式。", 12, MUTED))

# BC3/BC7
b.append(rect(600, 135, 545, 335, "#f8fafc", "#dbe4ee", 18))
b.append(text(623, 172, "BC3 / BC7：128 bit，4×4，RGBA 8 bpp", 19, INK, 700))
fields = [
    (623, 205, 240, "#dbeafe", BLUE, "颜色块", "64 bit"),
    (873, 205, 240, "#ffe4e6", ROSE, "Alpha / 模式块", "64 bit"),
]
for x, y, w, fill, color, title, sub in fields:
    b.append(rect(x, y, w, 66, fill, color, 8))
    b.append(text(x + w / 2, y + 28, title, 13, color, 700, "middle"))
    b.append(text(x + w / 2, y + 49, sub, 10, MUTED, 500, "middle"))
b.append(text(623, 310, "BC3：颜色块用 BC1 逻辑，Alpha 块存两个 8-bit 端点 + 16 个 3-bit 索引。", 13, MUTED))
b.append(text(623, 338, "BC7：128 bit 内有 8 种模式，可选 0–3 个分区，端点和索引位宽可变。", 13, MUTED))
b.append(text(623, 370, "BC6H：同尺寸，面向 HDR RGB，使用半精度端点和分区模式。", 13, MUTED))
b.append(text(623, 408, "解码核心仍然是：端点 + 分区 + 每 texel 索引/权重。", 14, BLUE, 600, "start", True))
b.append(text(623, 436, "但 BC7 的模式搜索明显更复杂，编码质量也更高。", 12, MUTED))

# family cards
families = [
    ("BC1", "RGB / 1-bit alpha", "64 bit · 4 bpp", BLUE),
    ("BC2", "RGB + 4-bit alpha", "128 bit · 8 bpp", TEAL),
    ("BC3", "RGB + smooth alpha", "128 bit · 8 bpp", ORANGE),
    ("BC4", "单通道", "64 bit · 4 bpp", PURPLE),
    ("BC5", "双通道 / 法线", "128 bit · 8 bpp", ROSE),
    ("BC6H", "HDR RGB", "128 bit · 8 bpp", AMBER),
    ("BC7", "高质量 RGBA", "128 bit · 8 bpp", GREEN),
]
for i, (name, desc, detail, color) in enumerate(families):
    x = 55 + (i % 4) * 272
    y = 510 + (i // 4) * 82
    w = 248
    b.append(rect(x, y, w, 65, color + "12", color, 10, 1.1))
    b.append(text(x + 13, y + 24, name, 15, color, 700))
    b.append(text(x + 13, y + 43, desc, 11, MUTED))
    b.append(text(x + w - 12, y + 43, detail, 9, color, 500, "end", True))
b.append(rect(55, 655, 1090, 32, "#f8fafc", "#dbe4ee", 10))
b.append(text(600, 676, "BC 主要面向 DirectX / 桌面 GPU；移动端支持取决于 GPU、图形 API 和压缩格式能力。", 12, MUTED, 400, "middle"))
save("06-bc.svg", 1200, 705, "BC 家族编码与解码", "".join(b))

