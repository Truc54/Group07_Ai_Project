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
        title = Text("Tổng kết", font=FONT, font_size=32, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # ── 3 Trụ cột (Thiết kế lại theo tone màu của từng cột, nội dung 1 dòng) ─
        pillars_data = [
            {
                "num":   "Trụ cột 1",
                "label": "Kiến trúc Tạo Video",
                "color": C_BLUE,
                "items": ["3D VAE", "Spatiotemporal Attention", "MVL Architecture"],
            },
            {
                "num":   "Trụ cột 2",
                "label": "Streaming Perception",
                "color": C_GREEN,
                "items": ["CUT3R", "Bộ nhớ 3D bền vững", "ST4rtrack 4D"],
            },
            {
                "num":   "Trụ cột 3",
                "label": "World Model cho Robot",
                "color": C_PURPLE,
                "items": ["Dữ liệu Internet", "Action Conditioning", "Vòng lặp tự cải tiến"],
            },
        ]

        pillar_groups = VGroup()

        for p in pillars_data:
            # Header text: cả num_text và label_text đều có màu tương tự khung (p["color"])
            num_text = Text(p["num"], font=FONT, font_size=14, color=p["color"], weight=BOLD)
            label_text = Text(p["label"], font=FONT, font_size=15, color=p["color"], weight=BOLD)
            header = VGroup(num_text, label_text).arrange(DOWN, buff=0.1)

            # Sub-items (đảm bảo hiển thị gọn gàng trên 1 dòng)
            sub_group = VGroup()
            for item_str in p["items"]:
                dot = Dot(radius=0.045, color=p["color"])
                dot.set_opacity(0.85)
                item_txt = Text(item_str, font=FONT, font_size=13, color=WHITE)
                item_txt.set_opacity(0.9)
                row = VGroup(dot, item_txt).arrange(RIGHT, buff=0.15)
                sub_group.add(row)
            sub_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

            # Gộp Header và Sub-items thành nội dung cột
            col_content = VGroup(header, sub_group).arrange(DOWN, buff=0.28)

            # Tạo khung (card) bao quanh toàn bộ nội dung cột
            card_rect = SurroundingRectangle(
                col_content,
                color=p["color"],
                fill_color=p["color"],
                fill_opacity=0.06,
                stroke_width=1.5,
                corner_radius=0.18,
                buff=0.32,
            )
            card_rect.set_stroke(color=p["color"], opacity=0.7, width=1.5)

            col = VGroup(card_rect, col_content)
            pillar_groups.add(col)

        pillar_groups.arrange(RIGHT, buff=0.4)
        pillar_groups.move_to(ORIGIN + UP * 0.25)

        # Animate từng trụ cột xuất hiện tuần tự
        for pg in pillar_groups:
            self.play(FadeIn(pg, shift=UP * 0.3), run_time=0.7)
            self.wait(0.15)

        self.wait(1.0)

        # ── Câu kết luận ─────────────────────────────────────────────────────
        conclusion = Text(
            "Tương lai của AI: không chỉ tạo hình ảnh đẹp — mà thực sự hiểu và tương tác với thế giới.",
            font=FONT, font_size=16, color=WHITE,
        )
        conclusion.set_opacity(0.9)
        conclusion.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)

        # ── Thu nhỏ và ẩn các trụ cột khi hiện câu cảm ơn (mất cột hoàn toàn) ─
        self.play(
            FadeOut(pillar_groups),
            FadeOut(conclusion),
            run_time=1.0,
        )

        thank_you = Text("Cảm ơn các bạn đã theo dõi!", font=FONT, font_size=40, color=WHITE, weight=BOLD)
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
            font=FONT, font_size=28, color=WHITE, weight=BOLD
        )
        video_title.to_edge(UP, buff=0.55)
        self.play(FadeIn(video_title, shift=DOWN * 0.2), run_time=0.8)

        # ── Đường kẻ ngang phân cách ─────────────────────────────────────────
        divider = Line(LEFT * 5.5, RIGHT * 5.5, color=WHITE, stroke_width=0.8)
        divider.set_opacity(0.3)
        divider.next_to(video_title, DOWN, buff=0.3)
        self.play(Create(divider), run_time=0.5)

        # ── Thành viên nhóm ───────────────────────────────────────────────────
        team_header = Text("NHÓM CODEX", font=FONT, font_size=20, color=WHITE, weight=BOLD)

        members = [
            ("Nguyễn Ngọc Minh Tuấn",  "MSSV: 23120102"),
            ("Trần Lê Trung Trực",    "MSSV: 23120180"),
        ]
        
        # Tạo hai cột riêng để MSSV được căn thẳng hàng
        names_list = []
        mssvs_list = []
        for name, mssv in members:
            names_list.append(Text(name, font=FONT, font_size=17, color=WHITE))
            mssvs_list.append(Text(mssv, font=FONT, font_size=15, color=WHITE).set_opacity(0.6))
            
        names_group = VGroup(*names_list).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        mssvs_group = VGroup(*mssvs_list)
        
        for i in range(len(members)):
            mssvs_group[i].align_to(names_group[i], UP)
            mssvs_group[i].align_to(names_group, LEFT).shift(RIGHT * 2.8)
            
        member_rows = VGroup(names_group, mssvs_group)
        team_block = VGroup(team_header, member_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ── Thông tin môn học ─────────────────────────────────────────────────
        course_header = Text("MÔN HỌC", font=FONT, font_size=20, color=WHITE, weight=BOLD)
        course_name = Text("Cơ sở Trí tuệ Nhân tạo", font=FONT, font_size=17, color=WHITE)
        course_time = Text("Học kỳ 2, năm học 2024–2025", font=FONT, font_size=15, color=WHITE)
        course_time.set_opacity(0.6)
        
        course_info = VGroup(course_name, course_time).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        course_block = VGroup(course_header, course_info).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # ── 2 cột: thành viên | môn học ──────────────────────────────────────
        two_cols = VGroup(team_block, course_block).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        two_cols.next_to(divider, DOWN, buff=0.4)
        self.play(FadeIn(two_cols, shift=UP * 0.15), run_time=0.9)
        self.wait(0.5)

        # ── Đường kẻ phân cách thứ 2 ─────────────────────────────────────────
        divider2 = Line(LEFT * 5.5, RIGHT * 5.5, color=WHITE, stroke_width=0.8)
        divider2.set_opacity(0.3)
        divider2.next_to(two_cols, DOWN, buff=0.35)
        self.play(Create(divider2), run_time=0.4)

        # ── Tài liệu tham khảo ───────────────────────────────────────────────
        ref_header = Text("TÀI LIỆU THAM KHẢO", font=FONT, font_size=18, color=WHITE, weight=BOLD)
        refs = [
            "CUT3R: Continuous 3D Perception (CVPR 2025)",
            "ST4rtrack: Simultaneous 4D Amodal Tracking (arXiv 2025)",
            "UniSim / Cosmos: World Foundation Models (NVIDIA 2024–2025)",
            "Wan 2.1 / CogVideoX / HunyuanVideo (2024–2025)",
        ]
        ref_items = VGroup()
        for r in refs:
            dot = Dot(radius=0.04, color=WHITE)
            dot.set_opacity(0.8)
            txt = Text(r, font=FONT, font_size=14, color=WHITE)
            txt.set_opacity(0.8)
            ref_items.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        ref_items.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ref_block = VGroup(ref_header, ref_items).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        ref_block.next_to(divider2, DOWN, buff=0.3)
        ref_block.align_to(team_block, LEFT)  # Căn thẳng hàng lề trái với Nhóm Codex
        self.play(FadeIn(ref_block, shift=UP * 0.1), run_time=0.8)

        # ── Footer: Made with Manim ──────────────────────────────────────────
        manim_txt = Text(
            "Made with Manim Community Edition",
            font=FONT, font_size=13, color=WHITE,
        )
        manim_txt.set_opacity(0.5)
        manim_txt.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(manim_txt), run_time=0.7)

        self.wait(3.0)

        self.play(*[FadeOut(m) for m in self.mobjects])