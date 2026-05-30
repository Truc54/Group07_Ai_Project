# scenes/part0_intro.py — Tuấn: Mở đầu (Sc01-03)
from manim import *
from scenes.config import *

# === SCENE 01 ===
class Scene01_Title(Scene):
    def construct(self):
        # TODO: Code animation cho Scene 01
        title = make_title("Từ Tạo Video AI", "Đến Mô hình Thế giới")
        self.play(Write(title))
        self.wait(2)

# === SCENE 02 ===
class Scene02_Importance(Scene):
    def construct(self):
        # TODO: Code animation cho Scene 02
        pass

# === SCENE 03 ===
class Scene03_Roadmap(Scene):
    def construct(self):
        # TODO: Code animation cho Scene 03
        pass
