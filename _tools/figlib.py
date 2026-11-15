# -*- coding: utf-8 -*-
"""Thư viện vẽ sơ đồ/lưu đồ bằng matplotlib cho báo cáo."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, Circle, FancyArrowPatch
from matplotlib import font_manager
import os

for f in ['C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/arialbd.ttf', 'C:/Windows/Fonts/ariali.ttf']:
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.unicode_minus'] = False

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# bảng màu
C_BLUE = '#1F4E79'
C_LBLUE = '#DCE9F5'
C_TEAL = '#0E7C7B'
C_LTEAL = '#D8F0EE'
C_ORANGE = '#C55A11'
C_LORANGE = '#FBE5D6'
C_GREEN = '#2E7D32'
C_LGREEN = '#E3F2E1'
C_RED = '#B71C1C'
C_LRED = '#FDE3E3'
C_GREY = '#595959'
C_LGREY = '#F2F2F2'
C_YEL = '#FFF4CC'
C_PURPLE = '#5B3A8C'
C_LPURPLE = '#E9E0F5'

STYLE = {
    'blue': (C_LBLUE, C_BLUE), 'teal': (C_LTEAL, C_TEAL), 'orange': (C_LORANGE, C_ORANGE),
    'green': (C_LGREEN, C_GREEN), 'red': (C_LRED, C_RED), 'grey': (C_LGREY, C_GREY),
    'yellow': (C_YEL, '#8A6D00'), 'purple': (C_LPURPLE, C_PURPLE), 'white': ('white', C_GREY),
}


def new_fig(w, h, dpi=200):
    fig = plt.figure(figsize=(w, h), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 10)
    ax.set_ylim(0, h * 10)
    ax.axis('off')
    ax.set_aspect('equal')
    return fig, ax


def save(fig, name):
    p = os.path.join(OUT, name + '.png')
    fig.savefig(p, dpi=200, facecolor='white')
    plt.close(fig)
    return p


def box(ax, x, y, w, h, text='', color='blue', fs=9, bold=False, rounded=True, lw=1.4, ha='center', tc=None, style=None):
    """x,y = tâm."""
    fc, ec = STYLE[color]
    if rounded:
        p = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=%s' % min(2.2, h / 4),
                           fc=fc, ec=ec, lw=lw, ls=style or '-')
    else:
        p = Rectangle((x - w / 2, y - h / 2), w, h, fc=fc, ec=ec, lw=lw, ls=style or '-')
    ax.add_patch(p)
    if text:
        tx = x if ha == 'center' else x - w / 2 + 1.5
        ax.text(tx, y, text, ha=ha, va='center', fontsize=fs, color=tc or '#1a1a1a',
                fontweight='bold' if bold else 'normal', linespacing=1.25)
    return p


def label(ax, x, y, text, fs=9, color='#1a1a1a', bold=False, ha='center', va='center', italic=False, rot=0):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=color, fontweight='bold' if bold else 'normal',
            fontstyle='italic' if italic else 'normal', linespacing=1.25, rotation=rot)


def arrow(ax, pts, color='#333333', lw=1.3, head=True, ls='-', both=False):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, ls=ls, solid_capstyle='butt')
    a = FancyArrowPatch(pts[-2], pts[-1], arrowstyle='-|>' if head else '-', mutation_scale=11,
                        color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    if both:
        b = FancyArrowPatch(pts[1], pts[0], arrowstyle='-|>', mutation_scale=11, color=color, lw=lw, shrinkA=0, shrinkB=0)
        ax.add_patch(b)


# ---------- lưu đồ ----------
class Flow:
    def __init__(self, w, h):
        self.fig, self.ax = new_fig(w, h)
        self.n = {}

    def node(self, key, x, y, kind, text, w=34, h=9, color=None, fs=8.5):
        self.n[key] = (x, y, w, h, kind)
        ax = self.ax
        col = color or {'term': 'green', 'proc': 'blue', 'dec': 'orange', 'io': 'teal', 'sub': 'purple'}[kind]
        fc, ec = STYLE[col]
        if kind == 'term':
            ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=%s' % (h / 2),
                                        fc=fc, ec=ec, lw=1.4))
        elif kind in ('proc', 'sub'):
            ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc=fc, ec=ec, lw=1.4))
            if kind == 'sub':
                ax.plot([x - w / 2 + 2, x - w / 2 + 2], [y - h / 2, y + h / 2], color=ec, lw=1)
                ax.plot([x + w / 2 - 2, x + w / 2 - 2], [y - h / 2, y + h / 2], color=ec, lw=1)
        elif kind == 'dec':
            ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True, fc=fc, ec=ec, lw=1.4))
        elif kind == 'io':
            s = 3
            ax.add_patch(Polygon([(x - w / 2 + s, y + h / 2), (x + w / 2, y + h / 2), (x + w / 2 - s, y - h / 2), (x - w / 2, y - h / 2)],
                                 closed=True, fc=fc, ec=ec, lw=1.4))
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, linespacing=1.2, color='#1a1a1a')

    def anchor(self, key, side):
        x, y, w, h, kind = self.n[key]
        return {'t': (x, y + h / 2), 'b': (x, y - h / 2), 'l': (x - w / 2, y), 'r': (x + w / 2, y)}[side]

    def edge(self, a, sa, b, sb, text=None, via=None, tpos=None, color='#333333'):
        p0 = self.anchor(a, sa)
        p1 = self.anchor(b, sb)
        pts = [p0] + (via or []) + [p1]
        arrow(self.ax, pts, color=color)
        if text:
            if tpos is None:
                tpos = (p0[0] + (3 if sa == 'r' else 0) + (-3 if sa == 'l' else 0), p0[1] - (2.2 if sa == 'b' else 0) + (2.2 if sa in 'rl' else 0))
            self.ax.text(tpos[0], tpos[1], text, fontsize=8, ha='center', va='center', color=C_ORANGE, fontweight='bold')

    def save(self, name):
        return save(self.fig, name)
