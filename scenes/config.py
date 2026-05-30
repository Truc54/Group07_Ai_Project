# scenes/config.py — DÙNG CHUNG CHO TẤT CẢ FILE SCENES
from manim import *

# === MÀU SẮC DỰ ÁN (PREMIUM AESTHETICS) ===
BG       = "#0f0f1a"
C_TITLE  = "#00d4ff"
C_SUB    = "#a0a0c0"
C_RED    = "#ff6b6b"
C_GREEN  = "#51cf66"
C_YELLOW = "#ffd43b"
C_PURPLE = "#e599f7"
C_BLUE   = "#74c0fc"
C_BOX    = "#1a1a2e"

FONT = "Arial"

def make_title(text, sub=""):
    """
    Tạo VGroup tiêu đề chuẩn hóa cho các Scene.
    """
    t = Text(text, font=FONT, font_size=42, color=C_TITLE).to_edge(UP, buff=0.5)
    if sub:
        s = Text(sub, font=FONT, font_size=28, color=C_SUB).next_to(t, DOWN, buff=0.3)
        return VGroup(t, s)
    return t

def make_box(text, w=4, h=1.5, color=C_BOX):
    """
    Tạo một hộp chữ nhật bo tròn góc có text ở trung tâm.
    """
    box = RoundedRectangle(width=w, height=h, corner_radius=0.2,
                           color=color, fill_opacity=0.3, stroke_color=color)
    label = Text(text, font=FONT, font_size=22, color=WHITE).move_to(box)
    return VGroup(box, label)

def make_bullets(items):
    """
    Tạo danh sách bullet points căn lề trái mượt mà.
    """
    lines = VGroup()
    for item in items:
        dot = Dot(radius=0.06, color=C_RED)
        txt = Text(item, font=FONT, font_size=22, color=WHITE)
        lines.add(VGroup(dot, txt).arrange(RIGHT, buff=0.3))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    return lines
