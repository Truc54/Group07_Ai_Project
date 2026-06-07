# scenes/part0_intro.py — Tuấn: Mở đầu (Sc01-03)
# Render toàn bộ: manim -pql scenes/part0_intro.py -a
# Render 1 scene: manim -pql scenes/part0_intro.py Scene01_Title
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 01 — Tiêu đề chính (~60s)                        ║
# ╚══════════════════════════════════════════════════════════╝
class Scene01_Title(Scene):
    def construct(self):
        self.camera.background_color = BG

        # === Tiêu đề chính ===
        main_title = Text(
            "Từ Tạo Video AI",
            font=FONT, font_size=56, color=WHITE, weight=BOLD
        )
        
        subtitle = Text(
            "Đến Mô hình Thế giới",
            font=FONT, font_size=56, color=C_GREEN, weight=BOLD
        )
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3).move_to(UP * 1.0)

        # Dòng phụ: Giao điểm của nhiều lĩnh vực
        description = Text(
            "Giao điểm của Computer Vision, Deep Learning, và Robotics",
            font=FONT, font_size=18, color=C_SUB
        ).next_to(title_group, DOWN, buff=0.8)

        # === Animation: Xuất hiện tiêu đề từng phần ===
        self.play(Write(main_title), run_time=1.5)
        self.wait(0.3)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(0.5)
        
        # Phụ đề xuất hiện với fade
        self.play(FadeIn(description, shift=UP * 0.2), run_time=1.0)
        self.wait(2)

        # === Hiệu ứng highlight: Viền quanh tiêu đề ===
        border_box = SurroundingRectangle(
            title_group, 
            color=C_BLUE, 
            buff=0.4, 
            stroke_width=2
        )
        
        self.play(Create(border_box), run_time=1.0)
        self.wait(1.5)

        # === Transition: Fade out toàn bộ ===
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 02 — Tại sao quan trọng? (~50s)                  ║
# ╚══════════════════════════════════════════════════════════╝
class Scene02_Importance(Scene):
    def construct(self):
        self.camera.background_color = BG

        # === Tiêu đề ===
        title = make_title("Tại sao chủ đề này quan trọng?")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Câu hỏi trung tâm lớn ===
        question = Text(
            "AI hiểu thế giới khi tạo video?",
            font=FONT, font_size=32, color=C_YELLOW, weight=BOLD
        ).shift(UP * 1.0)
        
        question_sub = Text(
            "Hay chỉ sao chép pixel?",
            font=FONT, font_size=32, color=C_YELLOW, weight=BOLD
        ).next_to(question, DOWN, buff=0.2)
        
        question_group = VGroup(question, question_sub)
        
        self.play(Write(question), run_time=1.2)
        self.play(Write(question_sub), run_time=1.0)
        self.wait(0.5)

        # === BÊN TRÁI: Pixel-Only (Sai) ===
        left_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.12,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        left_icon = Text("🎬", font_size=40)
        left_title = Text("Pixel-Only", font=FONT, font_size=16, color=C_RED, weight=BOLD)
        left_desc = VGroup(
            Text("Xuất hiện video đẹp", font=FONT, font_size=12, color=WHITE),
            Text("Nhưng thiếu hiểu biết", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.1)
        
        left_content = VGroup(left_icon, left_title, left_desc).arrange(DOWN, buff=0.15).move_to(left_box)
        left_group = VGroup(left_box, left_content)
        left_group.shift(LEFT * 4.5 + DOWN * 0.3)

        # === BÊN PHẢI: 3D Understanding (Đúng) ===
        right_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        )
        right_icon = Text("🧠", font_size=40)
        right_title = Text("3D Understanding", font=FONT, font_size=16, color=C_GREEN, weight=BOLD)
        right_desc = VGroup(
            Text("Hiểu cấu trúc 3D", font=FONT, font_size=12, color=WHITE),
            Text("Có tri thức thế giới", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.1)
        
        right_content = VGroup(right_icon, right_title, right_desc).arrange(DOWN, buff=0.15).move_to(right_box)
        right_group = VGroup(right_box, right_content)
        right_group.shift(RIGHT * 4.5 + DOWN * 0.3)

        # === Mũi tên so sánh ===
        vs_text = Text("VS", font=FONT, font_size=24, color=C_YELLOW, weight=BOLD)

        # === Animation ===
        self.play(FadeOut(question_group))
        self.play(
            FadeIn(left_group, shift=LEFT * 0.3),
            FadeIn(right_group, shift=RIGHT * 0.3),
            FadeIn(vs_text),
            run_time=1.2
        )
        self.wait(1.0)

        # === Dòng kết luận ===
        conclusion = Text(
            "→ Đây chính là câu hỏi mà các nhà nghiên cứu hàng đầu đang cố gắng trả lời",
            font=FONT, font_size=16, color=C_GREEN
        ).to_edge(DOWN, buff=1.0)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        self.wait(2)

        # === Transition ===
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 03 — Lộ trình video (~50s)                       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene03_Roadmap(Scene):
    def construct(self):
        self.camera.background_color = BG

        # === Tiêu đề ===
        title = make_title("Lộ trình của video")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === 3 Phần chính của video ===
        parts = [
            {
                "num": "PHẦN 1",
                "name": "Tạo Video AI",
                "items": ["3D VAE", "Spatiotemporal Attention", "Kiến trúc MVL"],
                "color": C_BLUE,
                "icon": "🎬"
            },
            {
                "num": "PHẦN 2",
                "name": "Nhận thức 3D",
                "items": ["CUT3R", "ST4rtrack", "Streaming Perception"],
                "color": C_PURPLE,
                "icon": "👁️"
            },
            {
                "num": "PHẦN 3",
                "name": "Mô hình Thế giới",
                "items": ["Dữ liệu lớn", "Action Conditioning", "Tự cải tiến"],
                "color": C_GREEN,
                "icon": "🤖"
            }
        ]

        # === Tạo 3 card cho mỗi phần ===
        cards = VGroup()
        for i, part in enumerate(parts):
            # Hộp chính
            card_box = RoundedRectangle(
                width=3.2, height=2.8, corner_radius=0.15,
                color=part["color"], fill_opacity=0.1, stroke_width=2
            )
            
            # Icon
            icon = Text(part["icon"], font_size=32).shift(UP * 0.8)
            
            # Số phần
            part_num = Text(part["num"], font=FONT, font_size=14, color=part["color"], weight=BOLD)
            
            # Tên phần
            part_name = Text(part["name"], font=FONT, font_size=16, color=WHITE, weight=BOLD)
            
            # Các mục chi tiết
            items_group = VGroup(*[
                Text(f"• {item}", font=FONT, font_size=11, color=C_SUB)
                for item in part["items"]
            ]).arrange(DOWN, buff=0.08)
            
            # Sắp xếp nội dung trong hộp
            content = VGroup(icon, part_num, part_name, items_group).arrange(DOWN, buff=0.15)
            content.move_to(card_box)
            
            cards.add(VGroup(card_box, content))

        # === Sắp xếp 3 card nằm ngang ===
        cards.arrange(RIGHT, buff=0.5).shift(UP * 0.2)

        # === Thanh tiến trình dưới (progress bar) ===
        progress_dots = VGroup()
        for i in range(3):
            dot_x = cards[i].get_center()[0]
            dot = Dot(point=[dot_x, -1.2, 0], radius=0.1, color=parts[i]["color"])
            progress_dots.add(dot)

        progress_line = Line(
            [cards[0].get_center()[0], -1.2, 0],
            [cards[2].get_center()[0], -1.2, 0],
            color=C_SUB, stroke_width=1.5
        )

        # === Animation: Xuất hiện từng card + thanh tiến trình ===
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.6)
            self.play(Create(progress_dots[i]), run_time=0.3)
            self.wait(0.2)

        self.play(Create(progress_line), run_time=0.5)
        self.wait(0.5)

        # === Lời kết ===
        outro_text = Text(
            "Nào, bắt đầu thôi!",
            font=FONT, font_size=28, color=C_GREEN, weight=BOLD
        ).to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(outro_text, scale=0.8), run_time=0.7)
        self.wait(1)

        # === Transition: Fade out toàn bộ ===
        self.play(*[FadeOut(m) for m in self.mobjects])
