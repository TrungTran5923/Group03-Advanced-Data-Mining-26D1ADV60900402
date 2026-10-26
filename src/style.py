"""Cấu hình biểu đồ dùng chung cho toàn đồ án (bảng màu đã kiểm tra an toàn cho người mù màu)."""
import matplotlib.pyplot as plt
import matplotlib as mpl

BLUE, ORANGE, AQUA, GRAY = "#2a78d6", "#eb6834", "#1baf7a", "#9a9890"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e6e5e0"

def setup():
    mpl.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlesize": 12,
        "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.titlelocation": "left",
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.axisbelow": True, "grid.color": GRID, "grid.linewidth": 0.8,
        "xtick.color": INK2, "ytick.color": INK2, "legend.frameon": False,
        "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight",
    })

def save(fig, name):
    fig.savefig(f"../figures/{name}.png", facecolor="white")
    plt.show()

def vn(x, d=0):
    """Định dạng số kiểu Việt Nam: 1.234.567,8"""
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
