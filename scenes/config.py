# scenes/config.py — DÙNG CHUNG CHO TẤT CẢ FILE SCENES
from manim import *

# === MÀU SẮC DỰ ÁN (PREMIUM AESTHETICS) ===
BG           = "#000000"  # Pure black background
C_TITLE      = "#F8FAFC"  # Bright white for titles
C_TEXT       = "#F8FAFC"  # Primary Text
C_TEXT_SUB   = "#94A3B8"  # Secondary Text / Muted Text
C_SUB        = "#94A3B8"  # Slate 400 for backward compatibility
C_RED        = "#EF4444"  # Danger/Challenge/Error
C_GREEN      = "#10B981"  # Success/Linear/Optimal
C_YELLOW     = "#F59E0B"  # Warning/Low-level/Amber
C_BLUE       = "#3B82F6"  # Primary/Blue (Task/General info)
C_PURPLE     = "#8B5CF6"  # Modern Violet
C_BOX        = "#1E293B"  # Slate 800 for card backgrounds

FONT = "Segoe UI"

def make_title(text, sub=""):
    """
    Tạo VGroup tiêu đề chuẩn hóa cho các Scene.
    """
    t = Text(text, font=FONT, font_size=42, color=C_TEXT).to_edge(UP, buff=0.8)
    if sub:
        s = Text(sub, font=FONT, font_size=28, color=C_TEXT_SUB).next_to(t, DOWN, buff=0.3)
        return VGroup(t, s)
    return t

def make_box(text, w=4, h=1.5, color=C_BOX, stroke_width=1.5, fill_opacity=0.08, font_size=22):
    """
    Tạo một hộp chữ nhật bo tròn góc có text ở trung tâm (Style Modern Tech).
    """
    box = RoundedRectangle(width=w, height=h, corner_radius=0.15,
                           color=color, fill_opacity=fill_opacity, stroke_width=stroke_width)
    label = Text(text, font=FONT, font_size=font_size, color=C_TEXT).move_to(box)
    return VGroup(box, label)

def make_bullets(items):
    """
    Tạo danh sách bullet points căn lề trái mượt mà.
    """
    lines = VGroup()
    for item in items:
        dot = Dot(radius=0.06, color=C_RED)
        txt = Text(item, font=FONT, font_size=22, color=C_TEXT)
        lines.add(VGroup(dot, txt).arrange(RIGHT, buff=0.3))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    return lines

def make_cross(size=0.3, stroke_width=3, color=C_RED):
    """
    Tạo dấu X (cross) chuyên nghiệp gồm 2 Line chéo nhau.
    """
    line1 = Line(LEFT * size / 2 + UP * size / 2, RIGHT * size / 2 + DOWN * size / 2, color=color, stroke_width=stroke_width)
    line2 = Line(LEFT * size / 2 + DOWN * size / 2, RIGHT * size / 2 + UP * size / 2, color=color, stroke_width=stroke_width)
    return VGroup(line1, line2)

