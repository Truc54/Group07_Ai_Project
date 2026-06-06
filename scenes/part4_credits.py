# scenes/part4_credits.py — Kết thúc (Sc45-46)
# Render toàn bộ: manim -pql scenes/part4_credits.py -a
# Render 1 scene: manim -pql scenes/part4_credits.py Scene45_Summary
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 45 — Tổng kết toàn video (~60s)                 ║
# ╚══════════════════════════════════════════════════════════╝
class Scene45_Summary(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Tiêu đề ──────────────────────────────────────────────────────────
        title = Text("Tổng kết", font=FONT, font_size=40, color=C_TITLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # ── 3 Trụ cột ────────────────────────────────────────────────────────
        pillars_data = [
            {
                "num":   "Trụ cột 1",
                "label": "Kiến trúc\nTạo Video",
                "color": C_BLUE,
                "items": ["3D VAE", "Spatiotemporal\nAttention", "MVL Architecture"],
            },
            {
                "num":   "Trụ cột 2",
                "label": "Streaming\nPerception",
                "color": C_GREEN,
                "items": ["CUT3R", "Bộ nhớ 3D\nbền vững", "ST4rtrack 4D"],
            },
            {
                "num":   "Trụ cột 3",
                "label": "World Model\ncho Robot",
                "color": C_PURPLE,
                "items": ["Dữ liệu Internet", "Action Conditioning\nLinear Projection", "Vòng lặp\ntự cải tiến"],
            },
        ]

        pillar_groups = VGroup()

        for p in pillars_data:
            # Header: content trước, box bao quanh sau
            num_text = Text(p["num"], font=FONT, font_size=17, color=p["color"])
            label_text = Text(p["label"], font=FONT, font_size=20, color=WHITE, line_spacing=1.2)
            header_content = VGroup(num_text, label_text).arrange(DOWN, buff=0.1)

            header_rect = SurroundingRectangle(
                header_content,
                color=p["color"],
                fill_color=p["color"],
                fill_opacity=0.15,
                stroke_width=2,
                corner_radius=0.18,
                buff=0.25,
            )
            header = VGroup(header_rect, header_content)

            # Sub-items
            sub_group = VGroup()
            for item_str in p["items"]:
                dot = Dot(radius=0.055, color=p["color"])
                item_txt = Text(item_str, font=FONT, font_size=16, color=C_SUB, line_spacing=1.2)
                row = VGroup(dot, item_txt).arrange(RIGHT, buff=0.2)
                sub_group.add(row)
            sub_group.arrange(DOWN, aligned_edge=LEFT, buff=0.22)

            col = VGroup(header, sub_group).arrange(DOWN, buff=0.25)
            pillar_groups.add(col)

        pillar_groups.arrange(RIGHT, buff=0.55)
        pillar_groups.move_to(ORIGIN + UP * 0.2)

        # Animate từng trụ cột xuất hiện tuần tự
        for pg in pillar_groups:
            self.play(FadeIn(pg, shift=UP * 0.3), run_time=0.7)
            self.wait(0.15)

        self.wait(1.0)

        # ── Câu kết luận ─────────────────────────────────────────────────────
        conclusion = Text(
            "Tương lai của AI: không chỉ tạo hình ảnh đẹp\n"
            "— mà thực sự hiểu và tương tác với thế giới.",
            font=FONT, font_size=21, color=C_YELLOW,
            line_spacing=1.4,
        )
        conclusion.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)

        # ── Merge animation: thu nhỏ, "Cảm ơn!" bùng lên ────────────────────
        self.play(
            pillar_groups.animate.scale(0.55).to_edge(UP, buff=1.1),
            FadeOut(conclusion),
            run_time=1.0,
        )

        thank_you = Text("Cảm ơn các bạn đã theo dõi!", font=FONT, font_size=44, color=C_TITLE)
        self.play(Write(thank_you), run_time=1.2)
        self.play(thank_you.animate.scale(1.08), run_time=0.4, rate_func=there_and_back)
        self.play(thank_you.animate.scale(1.05), run_time=0.35, rate_func=there_and_back)

        self.wait(2.0)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 46 — Credits (~40s)                             ║
# ╚══════════════════════════════════════════════════════════╝
class Scene46_Credits(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Tên video ─────────────────────────────────────────────────────────
        video_title = Text(
            "Từ Tạo Video AI đến Mô hình Thế giới",
            font=FONT, font_size=30, color=C_TITLE,
        )
        video_title.to_edge(UP, buff=0.55)
        self.play(FadeIn(video_title, shift=DOWN * 0.2), run_time=0.8)

        # ── Đường kẻ ngang phân cách ─────────────────────────────────────────
        divider = Line(LEFT * 5.5, RIGHT * 5.5, color=C_SUB, stroke_width=1)
        divider.next_to(video_title, DOWN, buff=0.3)
        self.play(Create(divider), run_time=0.5)

        # ── Thành viên nhóm ───────────────────────────────────────────────────
        team_header = Text("Nhóm CAF", font=FONT, font_size=22, color=C_YELLOW)

        members = [
            ("Nguyễn Ngọc Minh Tuấn",  "MSSV: 23120102"),
            ("Trần Lê Trung Trực",    "MSSV: 23120180"),
        ]
        member_rows = VGroup()
        for name, mssv in members:
            name_txt = Text(name, font=FONT, font_size=19, color=WHITE)
            mssv_txt = Text(mssv, font=FONT, font_size=17, color=C_SUB)
            row = VGroup(name_txt, mssv_txt).arrange(RIGHT, buff=0.6)
            member_rows.add(row)
        member_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        team_block = VGroup(team_header, member_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ── Thông tin môn học ─────────────────────────────────────────────────
        course_header = Text("Môn học", font=FONT, font_size=22, color=C_YELLOW)
        course_info = VGroup(
            Text("Big Data — Seminar Paper Presentation", font=FONT, font_size=19, color=WHITE),
            Text("Học kỳ 2, năm học 2024–2025", font=FONT, font_size=17, color=C_SUB),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        course_block = VGroup(course_header, course_info).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # ── 2 cột: thành viên | môn học ──────────────────────────────────────
        two_cols = VGroup(team_block, course_block).arrange(RIGHT, buff=1.5, aligned_edge=UP)
        two_cols.next_to(divider, DOWN, buff=0.45)
        self.play(FadeIn(two_cols, shift=UP * 0.15), run_time=0.9)
        self.wait(0.5)

        # ── Đường kẻ phân cách thứ 2 ─────────────────────────────────────────
        divider2 = Line(LEFT * 5.5, RIGHT * 5.5, color=C_SUB, stroke_width=1)
        divider2.next_to(two_cols, DOWN, buff=0.35)
        self.play(Create(divider2), run_time=0.4)

        # ── Tài liệu tham khảo ───────────────────────────────────────────────
        ref_header = Text("Tài liệu tham khảo", font=FONT, font_size=20, color=C_YELLOW)
        refs = [
            "CUT3R: Continuous 3D Perception (CVPR 2025)",
            "ST4rtrack: Simultaneous 4D Amodal Tracking (arXiv 2025)",
            "UniSim / Cosmos: World Foundation Models (NVIDIA 2024–2025)",
            "Wan 2.1 / CogVideoX / HunyuanVideo (2024–2025)",
        ]
        ref_items = VGroup()
        for r in refs:
            dot = Dot(radius=0.05, color=C_RED)
            txt = Text(r, font=FONT, font_size=15, color=C_SUB)
            ref_items.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        ref_items.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        ref_block = VGroup(ref_header, ref_items).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        ref_block.next_to(divider2, DOWN, buff=0.3)
        ref_block.to_edge(LEFT, buff=0.7)
        self.play(FadeIn(ref_block, shift=UP * 0.1), run_time=0.8)

        # ── Footer: GitHub + Made with Manim ─────────────────────────────────
        github_txt = Text(
            "GitHub: github.com/your-repo",
            font=FONT, font_size=16, color=C_BLUE,
        )
        manim_txt = Text(
            "Made with Manim Community Edition",
            font=FONT, font_size=15, color=C_SUB,
        )
        footer = VGroup(github_txt, manim_txt).arrange(RIGHT, buff=1.2)
        footer.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(footer), run_time=0.7)

        self.wait(3.0)

        self.play(*[FadeOut(m) for m in self.mobjects])