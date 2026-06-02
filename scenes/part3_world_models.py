# scenes/part3_world_models.py — Trực: Phần 3: Mô hình thế giới cho robot (Sc32-44)
# Render toàn bộ: manim -pql scenes/part3_world_models.py -a
# Render 1 scene: manim -pql scenes/part3_world_models.py Scene32_Part3Intro
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 32 — Giới thiệu Phần 3                          ║
# ╚══════════════════════════════════════════════════════════╝
class Scene32_Part3Intro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Tiêu đề phần
        part_num = Text("PHẦN 3", font=FONT, font_size=56, color=WHITE)
        line1 = Text("Mở rộng Mô hình Thế giới", font=FONT, font_size=38, color=WHITE)
        line2 = Text("cho Robot thông minh", font=FONT, font_size=38, color=WHITE)
        part_title = VGroup(line1, line2).arrange(DOWN, buff=0.2)
        part_group = VGroup(part_num, part_title).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(part_num, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(part_title), run_time=1.2)
        self.wait(1)

        # Chuyển sang nội dung tóm tắt
        self.play(FadeOut(part_group))

        desc1 = Text("Biến mô hình tạo video", font=FONT, font_size=26, color=WHITE)
        desc2 = Text("thành bộ giả lập thế giới cho robot", font=FONT, font_size=26, color=WHITE)
        desc_group = VGroup(desc1, desc2).arrange(DOWN, buff=0.2).move_to(ORIGIN)

        # Icon gợi ý
        robot_icon = Text("🤖", font_size=60).shift(LEFT * 3 + DOWN * 1.5)
        world_icon = Text("🌍", font_size=60).move_to(DOWN * 1.5)
        video_icon = Text("🎬", font_size=60).shift(RIGHT * 3 + DOWN * 1.5)

        self.play(FadeIn(desc_group), run_time=1)
        self.wait(0.5)
        self.play(
            FadeIn(robot_icon, shift=UP * 0.3),
            FadeIn(world_icon, shift=UP * 0.3),
            FadeIn(video_icon, shift=UP * 0.3),
            run_time=0.8
        )
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 33 — Bối cảnh lịch sử World Models               ║
# ╚══════════════════════════════════════════════════════════╝
class Scene33_HistoricalContext(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Bối cảnh lịch sử", "Từ RL đến World Models quy mô lớn")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Timeline
        line = Line(LEFT * 5.5, RIGHT * 5.5, color=C_SUB, stroke_width=2).shift(UP * 0.3)
        self.play(Create(line))

        milestones = [
            ("2018", "World Models\n(Ha & Schmidhuber)", C_BLUE),
            ("2020", "Dreamer V1", C_PURPLE),
            ("2023", "Dreamer V3", C_PURPLE),
            ("2024-25", "Internet-scale\nWorld Models", C_GREEN),
        ]

        positions = [LEFT * 4.2, LEFT * 1.4, RIGHT * 1.4, RIGHT * 4.2]

        for i, ((year, desc, col), pos) in enumerate(zip(milestones, positions)):
            dot = Dot(point=pos + UP * 0.3, radius=0.12, color=col)
            y_label = Text(year, font=FONT, font_size=20, color=WHITE).next_to(dot, DOWN, buff=0.25)

            desc_lines = desc.split("\n")
            d_label = VGroup(*[
                Text(l, font=FONT, font_size=14, color=WHITE) for l in desc_lines
            ]).arrange(DOWN, buff=0.1).next_to(y_label, DOWN, buff=0.15)

            self.play(FadeIn(dot, scale=0.5), FadeIn(y_label), run_time=0.5)
            self.play(FadeIn(d_label, shift=UP * 0.2), run_time=0.4)

        # Mũi tên bước nhảy lớn
        jump_arrow = Arrow(
            RIGHT * 2.0 + DOWN * 0.6, RIGHT * 3.5 + DOWN * 0.6,
            color=C_YELLOW, stroke_width=3
        )
        jump_label = Text("Bước nhảy lớn!", font=FONT, font_size=16, color=C_YELLOW)
        jump_label.next_to(jump_arrow, DOWN, buff=0.15)
        self.play(Create(jump_arrow), FadeIn(jump_label), run_time=0.6)

        # Hai yếu tố khác biệt
        factor_box = RoundedRectangle(
            width=10, height=1.2, corner_radius=0.15,
            color=C_BOX, fill_opacity=0.3, stroke_width=1.5
        ).to_edge(DOWN, buff=0.5)
        factor_text = Text(
            "2 yếu tố: Dữ liệu quy mô Internet + Kiến trúc mở rộng mạnh",
            font=FONT, font_size=18, color=WHITE
        ).move_to(factor_box)
        self.play(FadeIn(factor_box), FadeIn(factor_text))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 34 — 21 triệu cặp Video-Hành động: Tổng quan    ║
# ╚══════════════════════════════════════════════════════════╝
class Scene34_DatasetOverview(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Dữ liệu quy mô lớn cho World Model")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Con số ấn tượng
        number_text = Text("21,000,000", font=FONT, font_size=72, color=C_YELLOW, weight=BOLD)
        number_text.move_to(UP * 0.8)
        sub_text = Text(
            "cặp Video-Hành động được căn chỉnh theo thời gian",
            font=FONT, font_size=22, color=WHITE
        ).next_to(number_text, DOWN, buff=0.3)

        self.play(FadeIn(number_text, scale=0.5), run_time=1)
        self.play(FadeIn(sub_text), run_time=0.6)
        self.wait(1)

        # "Time-Aligned" highlight
        aligned_box = RoundedRectangle(
            width=5, height=1.0, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.12, stroke_width=2
        ).shift(DOWN * 1.0)
        aligned_text = Text(
            "Time-Aligned: Mỗi hành động khớp chính xác với từng frame",
            font=FONT, font_size=18, color=WHITE
        ).move_to(aligned_box)
        self.play(FadeIn(aligned_box), FadeIn(aligned_text), run_time=0.8)
        self.wait(0.5)

        # 4 icon nguồn
        sources = VGroup(
            Text("🔤", font_size=36),
            Text("🎥", font_size=36),
            Text("🤖", font_size=36),
            Text("⌨️", font_size=36),
        ).arrange(RIGHT, buff=1.2).shift(DOWN * 2.5)
        source_labels = VGroup(
            Text("Text", font=FONT, font_size=14, color=WHITE),
            Text("Camera", font=FONT, font_size=14, color=WHITE),
            Text("Robot", font=FONT, font_size=14, color=WHITE),
            Text("Keyboard", font=FONT, font_size=14, color=WHITE),
        )
        for icon, label in zip(sources, source_labels):
            label.next_to(icon, DOWN, buff=0.15)

        self.play(
            LaggedStart(*[FadeIn(s, scale=0.5) for s in sources], lag_ratio=0.15),
            LaggedStart(*[FadeIn(l) for l in source_labels], lag_ratio=0.15),
        )

        # Ý tưởng cốt lõi
        core_idea = Text(
            "Video = Ngôn ngữ chung cho việc ra quyết định",
            font=FONT, font_size=20, color=C_YELLOW
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(core_idea))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 35 — 4 loại dữ liệu chi tiết                    ║
# ╚══════════════════════════════════════════════════════════╝
class Scene35_FourDataTypes(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("4 nguồn dữ liệu chi tiết")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        data_types = [
            ("🔤", "Text-Video", "Video + mô tả hành động", C_BLUE),
            ("🎥", "Camera Control", "Video + thông tin xoay 360°", C_GREEN),
            ("🤖", "Robot Control", "Video + vector vận tốc Δx, Δy", C_YELLOW),
            ("⌨️", "Keyboard Control", "Video game + lịch sử nhấn phím", C_PURPLE),
        ]

        cards = VGroup()
        for icon_text, type_name, example, col in data_types:
            box = RoundedRectangle(
                width=2.6, height=3.0, corner_radius=0.15,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            icon = Text(icon_text, font_size=36).move_to(box.get_top() + DOWN * 0.5)
            name = Text(type_name, font=FONT, font_size=16, color=WHITE, weight=BOLD)
            name.next_to(icon, DOWN, buff=0.25)

            # Ví dụ - chia dòng nếu cần
            ex_lines = example.split(" + ")
            ex_group = VGroup(*[
                Text(l, font=FONT, font_size=12, color=C_SUB) for l in ex_lines
            ]).arrange(DOWN, buff=0.08).next_to(name, DOWN, buff=0.25)

            cards.add(VGroup(box, icon, name, ex_group))

        cards.arrange(RIGHT, buff=0.25).shift(DOWN * 0.3)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.6)
            self.wait(0.3)

        conclusion = Text(
            "→ Sự đa dạng giúp mô hình học được quy luật vật lý tổng quát",
            font=FONT, font_size=20, color=WHITE
        ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 36 — Action Conditioning: Thách thức              ║
# ╚══════════════════════════════════════════════════════════╝
class Scene36_ActionChallenge(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Action Conditioning", "Đưa hành động robot vào mô hình video")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Câu hỏi trung tâm
        question = Text(
            "Thách thức: Làm sao đưa continuous action vào video diffusion model?",
            font=FONT, font_size=20, color=C_YELLOW
        ).shift(UP * 1.2)
        self.play(FadeIn(question), run_time=0.8)
        self.wait(0.5)

        # Phương pháp sai: Discretization
        wrong1_box = RoundedRectangle(
            width=4.5, height=2.5, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        w1_title = Text("Discretization / Text Embedding", font=FONT, font_size=16, color=WHITE, weight=BOLD)
        w1_steps = VGroup(
            Text("Vector liên tục → Rời rạc hóa", font=FONT, font_size=14, color=WHITE),
            Text("hoặc Text encode (CLIP/T5)", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        w1_result = Text("Robot giật cục, sai lệch vị trí", font=FONT, font_size=14, color=C_RED)
        w1_content = VGroup(w1_title, w1_steps, w1_result).arrange(DOWN, buff=0.25).move_to(wrong1_box)
        wrong1_group = VGroup(wrong1_box, w1_content)

        # Dấu X
        cross1 = make_cross(size=0.5, stroke_width=4, color=C_RED)
        cross1.next_to(wrong1_box, RIGHT, buff=0.3)

        # Phương pháp sai: Text embedding
        wrong2_box = RoundedRectangle(
            width=4.5, height=2.5, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        w2_title = Text("Text Embedding (TinyLlama/CLIP)", font=FONT, font_size=16, color=WHITE, weight=BOLD)
        w2_steps = VGroup(
            Text("Vector → Text encode → Mô hình", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        w2_result = Text("Vật lý bị drift hoàn toàn", font=FONT, font_size=14, color=C_RED)
        w2_content = VGroup(w2_title, w2_steps, w2_result).arrange(DOWN, buff=0.25).move_to(wrong2_box)
        wrong2_group = VGroup(wrong2_box, w2_content)

        cross2 = make_cross(size=0.5, stroke_width=4, color=C_RED)
        cross2.next_to(wrong2_box, RIGHT, buff=0.3)

        # Sắp xếp 2 phương pháp sai
        wrong_pair = VGroup(
            VGroup(wrong1_group, cross1),
            VGroup(wrong2_group, cross2)
        ).arrange(RIGHT, buff=0.6).shift(DOWN * 0.5)

        self.play(FadeIn(wrong1_group, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(cross1, scale=0.5))
        self.wait(0.5)
        self.play(FadeIn(wrong2_group, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(cross2, scale=0.5))

        conclusion = Text(
            "→ Cả hai phương pháp đều làm robot di chuyển sai lệch nghiêm trọng!",
            font=FONT, font_size=18, color=C_RED
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 37 — Action Conditioning: Linear Projection       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene37_LinearProjection(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Giải pháp: Linear Projection", "Đơn giản nhưng hiệu quả nhất")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Công thức
        formula_label = Text("Công thức:", font=FONT, font_size=22, color=WHITE)
        formula = MathTex(
            r"\vec{h}_a = W \cdot \vec{a}",
            font_size=48, color=WHITE
        )
        formula_group = VGroup(formula_label, formula).arrange(RIGHT, buff=0.4).shift(UP * 1.2)

        self.play(FadeIn(formula_label), run_time=0.5)
        self.play(Write(formula), run_time=1)
        self.wait(0.5)

        # Giải thích công thức
        explain_items = [
            (MathTex(r"\vec{a}", font_size=30, color=C_BLUE), "= raw action vector (vận tốc, lực)"),
            (MathTex(r"W", font_size=30, color=C_YELLOW), "= weight matrix (học được)"),
            (MathTex(r"\vec{h}_a", font_size=30, color=C_GREEN), "= action feature → cộng vào latent space"),
        ]

        explains = VGroup()
        for math_tex, desc in explain_items:
            desc_text = Text(desc, font=FONT, font_size=16, color=WHITE)
            row = VGroup(math_tex, desc_text).arrange(RIGHT, buff=0.3)
            explains.add(row)
        explains.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.2)

        for exp in explains:
            self.play(FadeIn(exp, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)

        # So sánh kết quả
        self.wait(0.5)
        compare_box_width = 4.5
        compare_box_height = 1.3

        # Kết quả xấu
        bad_box = RoundedRectangle(
            width=compare_box_width, height=compare_box_height, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=1.5
        )
        bad_label = Text("Discretization", font=FONT, font_size=16, color=WHITE, weight=BOLD)
        bad_result = Text("Robot giật cục, sai lệch ✗", font=FONT, font_size=14, color=C_RED)
        bad_content = VGroup(bad_label, bad_result).arrange(DOWN, buff=0.15).move_to(bad_box)
        bad_group = VGroup(bad_box, bad_content)

        # Kết quả tốt
        good_box = RoundedRectangle(
            width=compare_box_width, height=compare_box_height, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.08, stroke_width=1.5
        )
        good_label = Text("Linear Projection", font=FONT, font_size=16, color=WHITE, weight=BOLD)
        good_result = Text("Robot mượt mà, chính xác ✓", font=FONT, font_size=14, color=C_GREEN)
        good_content = VGroup(good_label, good_result).arrange(DOWN, buff=0.15).move_to(good_box)
        good_group = VGroup(good_box, good_content)

        compare = VGroup(bad_group, good_group).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(compare), run_time=0.8)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 38 — Video Language Planning: Ý tưởng            ║
# ╚══════════════════════════════════════════════════════════╝
class Scene38_VLP_Idea(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Video Language Planning (VLP)", "Lập kế hoạch phân cấp cho robot")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Nhiệm vụ lớn
        task_box = RoundedRectangle(
            width=9, height=1.2, corner_radius=0.15,
            color=C_BLUE, fill_opacity=0.1, stroke_width=2
        ).shift(UP * 1.0)
        task_text = Text(
            "Nhiệm vụ: \"Dọn dẹp bàn ăn và cất quả táo vào ngăn kéo\"",
            font=FONT, font_size=18, color=WHITE
        ).move_to(task_box)
        self.play(FadeIn(task_box), FadeIn(task_text), run_time=0.8)
        self.wait(0.5)

        # Dấu hỏi
        question = Text("Làm sao sinh video dài\nthể hiện toàn bộ quá trình?",
                         font=FONT, font_size=20, color=C_YELLOW)
        question.shift(DOWN * 0.3)
        self.play(FadeIn(question), run_time=0.8)
        self.wait(1)

        # Vấn đề
        problem = Text(
            "→ Sinh video dài trong 1 lượt → suy giảm chất lượng nghiêm trọng!",
            font=FONT, font_size=18, color=C_RED
        ).shift(DOWN * 1.3)
        self.play(FadeIn(problem))
        self.wait(1)

        # Giải pháp
        solution_box = RoundedRectangle(
            width=8, height=1.2, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.12, stroke_width=2
        ).to_edge(DOWN, buff=0.6)
        solution_text = Text(
            "Giải pháp: VLP — Lập kế hoạch phân cấp kết hợp Ngôn ngữ + Video",
            font=FONT, font_size=18, color=WHITE
        ).move_to(solution_box)
        self.play(FadeIn(solution_box), FadeIn(solution_text), run_time=0.8)
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 39 — VLP: 3 cấp chi tiết                         ║
# ╚══════════════════════════════════════════════════════════╝
class Scene39_VLP_ThreeLevels(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("VLP: Lập kế hoạch 3 cấp")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        levels = [
            ("Cấp cao — LLM", "Phân rã nhiệm vụ thành hành động chữ",
             "Bước 1: Mở ngăn kéo\nBước 2: Bỏ táo vào\nBước 3: Đóng ngăn kéo", C_BLUE),
            ("Cấp trung — Text-to-Video", "Sinh video ngắn cho mỗi bước",
             "Universal Policy:\nvideo thể hiện robot\nhoàn thành từng bước", C_GREEN),
            ("Cấp thấp — Inverse Dynamics", "Dịch video → motor commands",
             "Optical flow → vector\nvận tốc gửi đến khớp robot", C_YELLOW),
        ]

        level_groups = VGroup()
        for level_name, level_desc, example, col in levels:
            box = RoundedRectangle(
                width=10.5, height=1.8, corner_radius=0.15,
                color=col, fill_opacity=0.08, stroke_width=2
            )
            # Tiêu đề bên trái
            name_text = Text(level_name, font=FONT, font_size=18, color=WHITE, weight=BOLD)
            desc_text = Text(level_desc, font=FONT, font_size=14, color=C_SUB)
            left_col = VGroup(name_text, desc_text).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

            # Ví dụ bên phải
            ex_lines = example.split("\n")
            ex_group = VGroup(*[
                Text(l, font=FONT, font_size=12, color=WHITE) for l in ex_lines
            ]).arrange(DOWN, buff=0.06)

            inner = VGroup(left_col, ex_group).arrange(RIGHT, buff=1.5).move_to(box)
            level_groups.add(VGroup(box, inner))

        level_groups.arrange(DOWN, buff=0.15).shift(DOWN * 0.3)

        # Mũi tên nối giữa các cấp
        arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                level_groups[i].get_bottom(), level_groups[i + 1].get_top(),
                color=C_SUB, stroke_width=2, buff=0.05,
                max_tip_length_to_length_ratio=0.3
            )
            arrows.add(arr)

        for i, lg in enumerate(level_groups):
            self.play(FadeIn(lg, shift=RIGHT * 0.3), run_time=0.7)
            if i < 2:
                self.play(Create(arrows[i]), run_time=0.3)
            self.wait(0.3)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 40 — Đánh giá Robot: Vấn đề                      ║
# ╚══════════════════════════════════════════════════════════╝
class Scene40_EvalProblem(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Đánh giá Robot Policy", "Vấn đề của phương pháp cũ")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Phương pháp 1: Robot thật
        real_box = RoundedRectangle(
            width=4.5, height=2.5, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        real_icon = Text("🤖", font_size=40).move_to(real_box.get_top() + DOWN * 0.5)
        real_title = Text("Robot thật", font=FONT, font_size=20, color=WHITE, weight=BOLD)
        real_title.next_to(real_icon, DOWN, buff=0.2)
        real_issues = VGroup(
            Text("• Cực kỳ đắt đỏ ($$$)", font=FONT, font_size=14, color=WHITE),
            Text("• Robot có thể bị hỏng", font=FONT, font_size=14, color=WHITE),
            Text("• Tốn thời gian vận hành", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(real_title, DOWN, buff=0.2)
        real_group = VGroup(real_box, real_icon, real_title, real_issues)
        cross1 = make_cross(size=0.5, stroke_width=4, color=C_RED)
        cross1.next_to(real_box, UR, buff=-0.3)

        # Phương pháp 2: Simulator
        sim_box = RoundedRectangle(
            width=4.5, height=2.5, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        sim_icon = Text("💻", font_size=40).move_to(sim_box.get_top() + DOWN * 0.5)
        sim_title = Text("Simulator truyền thống", font=FONT, font_size=20, color=WHITE, weight=BOLD)
        sim_title.next_to(sim_icon, DOWN, buff=0.2)
        sim_issues = VGroup(
            Text("• Sim-to-real gap quá lớn", font=FONT, font_size=14, color=WHITE),
            Text("• Kết quả không tương quan thực tế", font=FONT, font_size=14, color=WHITE),
            Text("• Vật lý mô phỏng quá đơn giản", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(sim_title, DOWN, buff=0.2)
        sim_group = VGroup(sim_box, sim_icon, sim_title, sim_issues)
        cross2 = make_cross(size=0.5, stroke_width=4, color=C_RED)
        cross2.next_to(sim_box, UR, buff=-0.3)

        pair = VGroup(
            VGroup(real_group, cross1),
            VGroup(sim_group, cross2)
        ).arrange(RIGHT, buff=0.6).shift(DOWN * 0.3)

        self.play(FadeIn(real_group, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(cross1, scale=0.5))
        self.wait(0.5)
        self.play(FadeIn(sim_group, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(cross2, scale=0.5))

        conclusion = Text(
            "→ Cần phương pháp đánh giá mới: rẻ, nhanh, sát thực tế!",
            font=FONT, font_size=18, color=C_YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 41 — Đánh giá Robot: Dùng Mô hình Thế giới       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene41_EvalWorldModel(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Đánh giá bằng Mô hình Thế giới")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Pipeline: Robot Policy → World Model → Video → VLM → Score
        steps = [
            ("Robot\nPolicy", C_BLUE),
            ("World\nModel", C_GREEN),
            ("Video\ngiả lập", C_YELLOW),
            ("VLM\n(chấm điểm)", C_PURPLE),
            ("Score\n✓ / ✗", C_RED),
        ]

        step_boxes = VGroup()
        for step_name, col in steps:
            box = RoundedRectangle(
                width=2.0, height=1.5, corner_radius=0.12,
                color=col, fill_opacity=0.12, stroke_width=2
            )
            name_lines = step_name.split("\n")
            label = VGroup(*[
                Text(l, font=FONT, font_size=14, color=WHITE) for l in name_lines
            ]).arrange(DOWN, buff=0.08).move_to(box)
            step_boxes.add(VGroup(box, label))

        step_boxes.arrange(RIGHT, buff=0.3).shift(DOWN * 0.2)

        # Animate từng bước + mũi tên
        self.play(FadeIn(step_boxes[0], scale=0.8), run_time=0.5)
        for i in range(1, len(step_boxes)):
            arr = Arrow(
                step_boxes[i - 1].get_right(), step_boxes[i].get_left(),
                color=C_SUB, stroke_width=2, buff=0.05,
                max_tip_length_to_length_ratio=0.4
            )
            self.play(Create(arr), FadeIn(step_boxes[i], shift=LEFT * 0.2), run_time=0.4)

        self.wait(0.5)

        # Giải thích
        explain = VGroup(
            Text("1. Chạy hành động vào World Model → sinh video giả lập", font=FONT, font_size=16, color=WHITE),
            Text("2. VLM đánh giá: nhiệm vụ thành công hay thất bại?", font=FONT, font_size=16, color=WHITE),
            Text("→ Không cần robot thật, không có sim-to-real gap!", font=FONT, font_size=16, color=C_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=0.6)

        for line in explain:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 42 — False Negative & False Positive              ║
# ╚══════════════════════════════════════════════════════════╝
class Scene42_FalseErrors(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("2 loại lỗi chí mạng")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # === FALSE NEGATIVE ===
        fn_box = RoundedRectangle(
            width=5.0, height=3.2, corner_radius=0.15,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=2
        )
        fn_title = Text("False Negative", font=FONT, font_size=20, color=C_YELLOW, weight=BOLD)
        fn_title.move_to(fn_box.get_top() + DOWN * 0.35)

        fn_steps = VGroup(
            Text("Robot hành động ĐÚNG ✓", font=FONT, font_size=14, color=C_GREEN),
            Text("↓", font_size=20, color=WHITE),
            Text("World Model render video LỖI", font=FONT, font_size=14, color=C_RED),
            Text("↓", font_size=20, color=WHITE),
            Text("VLM đánh giá: THẤT BẠI ✗", font=FONT, font_size=14, color=C_RED),
        ).arrange(DOWN, buff=0.1).move_to(fn_box).shift(DOWN * 0.15)

        fn_group = VGroup(fn_box, fn_title, fn_steps)

        # === FALSE POSITIVE ===
        fp_box = RoundedRectangle(
            width=5.0, height=3.2, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.08, stroke_width=2
        )
        fp_title = Text("False Positive", font=FONT, font_size=20, color=C_PURPLE, weight=BOLD)
        fp_title.move_to(fp_box.get_top() + DOWN * 0.35)

        fp_steps = VGroup(
            Text("Robot hành động SAI ✗", font=FONT, font_size=14, color=C_RED),
            Text("↓", font_size=20, color=WHITE),
            Text("World Model tự \"sửa sai\" video", font=FONT, font_size=14, color=C_YELLOW),
            Text("↓", font_size=20, color=WHITE),
            Text("VLM đánh giá: THÀNH CÔNG ✓", font=FONT, font_size=14, color=C_GREEN),
        ).arrange(DOWN, buff=0.1).move_to(fp_box).shift(DOWN * 0.15)

        fp_group = VGroup(fp_box, fp_title, fp_steps)

        errors = VGroup(fn_group, fp_group).arrange(RIGHT, buff=0.5).shift(DOWN * 0.1)

        # Animate
        self.play(FadeIn(fn_group, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(1)
        self.play(FadeIn(fp_group, shift=LEFT * 0.3), run_time=0.8)
        self.wait(0.5)

        warning = Text(
            "→ Cả hai lỗi đều nguy hiểm, cần cơ chế tự cải tiến!",
            font=FONT, font_size=18, color=C_RED
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(warning))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 43 — Vòng lặp tự cải tiến                        ║
# ╚══════════════════════════════════════════════════════════╝
class Scene43_SelfImproving(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vòng lặp tự cải tiến", "Self-Improving World Model")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Trung tâm: World Model
        center_box = RoundedRectangle(
            width=3.5, height=1.5, corner_radius=0.2,
            color=C_GREEN, fill_opacity=0.15, stroke_width=2
        ).move_to(ORIGIN)
        center_label = Text("World Model", font=FONT, font_size=22, color=WHITE, weight=BOLD)
        center_label.move_to(center_box)
        center_sub = Text("(tốt hơn)", font=FONT, font_size=14, color=C_GREEN)
        center_sub.next_to(center_box, DOWN, buff=0.1)

        self.play(FadeIn(center_box), FadeIn(center_label), FadeIn(center_sub), run_time=0.8)
        self.wait(0.5)

        # === Nhánh 1: AI Feedback (bên trái) ===
        ai_title = Text("Cơ chế 1: AI Feedback", font=FONT, font_size=18, color=C_BLUE, weight=BOLD)
        ai_title.move_to(LEFT * 4 + UP * 2.2)

        ai_steps = VGroup(
            make_box("Video sinh ra", w=2.8, h=0.8, color=C_BLUE),
            make_box("VLM chấm điểm", w=2.8, h=0.8, color=C_BLUE),
            make_box("DPO huấn luyện", w=2.8, h=0.8, color=C_BLUE),
        ).arrange(DOWN, buff=0.15).move_to(LEFT * 4 + DOWN * 0.2)

        ai_arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                ai_steps[i].get_bottom(), ai_steps[i + 1].get_top(),
                color=C_BLUE, stroke_width=1.5, buff=0.05,
                max_tip_length_to_length_ratio=0.3
            )
            ai_arrows.add(arr)

        # Mũi tên từ DPO về World Model
        ai_return = Arrow(
            ai_steps[2].get_right(), center_box.get_left(),
            color=C_BLUE, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(FadeIn(ai_title), run_time=0.5)
        for i, step in enumerate(ai_steps):
            self.play(FadeIn(step, shift=DOWN * 0.2), run_time=0.4)
            if i < 2:
                self.play(Create(ai_arrows[i]), run_time=0.2)
        self.play(Create(ai_return), run_time=0.5)
        self.wait(0.5)

        # === Nhánh 2: Execution Feedback (bên phải) ===
        exec_title = Text("Cơ chế 2: Execution Feedback", font=FONT, font_size=18, color=C_YELLOW, weight=BOLD)
        exec_title.move_to(RIGHT * 4 + UP * 2.2)

        exec_steps = VGroup(
            make_box("Robot thực thi", w=2.8, h=0.8, color=C_YELLOW),
            make_box("Dữ liệu phản hồi", w=2.8, h=0.8, color=C_YELLOW),
            make_box("DAgger / STaR", w=2.8, h=0.8, color=C_YELLOW),
        ).arrange(DOWN, buff=0.15).move_to(RIGHT * 4 + DOWN * 0.2)

        exec_arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                exec_steps[i].get_bottom(), exec_steps[i + 1].get_top(),
                color=C_YELLOW, stroke_width=1.5, buff=0.05,
                max_tip_length_to_length_ratio=0.3
            )
            exec_arrows.add(arr)

        # Mũi tên từ DAgger về World Model
        exec_return = Arrow(
            exec_steps[2].get_left(), center_box.get_right(),
            color=C_YELLOW, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(FadeIn(exec_title), run_time=0.5)
        for i, step in enumerate(exec_steps):
            self.play(FadeIn(step, shift=DOWN * 0.2), run_time=0.4)
            if i < 2:
                self.play(Create(exec_arrows[i]), run_time=0.2)
        self.play(Create(exec_return), run_time=0.5)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 44 — Recap Phần 3                                ║
# ╚══════════════════════════════════════════════════════════╝
class Scene44_Part3Recap(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Tổng kết Phần 3")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 3 keyword recap
        keywords = [
            ("Dữ liệu\nquy mô lớn", "21 triệu cặp\ntime-aligned data", C_BLUE),
            ("Action\nConditioning", "Linear Projection\nh_a = W · a", C_GREEN),
            ("Tự cải tiến", "AI Feedback\n+ Execution Feedback", C_YELLOW),
        ]

        kw_cards = VGroup()
        for kw_title, kw_desc, col in keywords:
            box = RoundedRectangle(
                width=3.2, height=2.8, corner_radius=0.15,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            # Title
            t_lines = kw_title.split("\n")
            t = VGroup(*[
                Text(line, font=FONT, font_size=18, color=WHITE) for line in t_lines
            ]).arrange(DOWN, buff=0.1).move_to(box.get_top() + DOWN * 0.6)

            # Description
            d_lines = kw_desc.split("\n")
            d = VGroup(*[
                Text(line, font=FONT, font_size=14, color=WHITE) for line in d_lines
            ]).arrange(DOWN, buff=0.1).move_to(box.get_center() + DOWN * 0.3)

            check = Text("✓", font_size=28, color=col).move_to(box.get_bottom() + UP * 0.35)
            kw_cards.add(VGroup(box, t, d, check))

        kw_cards.arrange(RIGHT, buff=0.3).shift(UP * 0.1)

        for card in kw_cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.5)
            self.wait(0.3)

        self.wait(1)

        # Sơ đồ tổng hợp nhỏ ở dưới
        summary_box = RoundedRectangle(
            width=10, height=1.5, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.4)

        summary = VGroup(
            Text("VLP giúp robot thực hiện nhiệm vụ dài hạn", font=FONT, font_size=18, color=WHITE),
            Text("World Model đóng vai trò bộ giả lập để đánh giá robot policy", font=FONT, font_size=18, color=WHITE),
        ).arrange(DOWN, buff=0.15).move_to(summary_box)

        self.play(FadeIn(summary_box), FadeIn(summary), run_time=1)
        self.wait(2)

        # Transition
        self.play(
            *[FadeOut(card, shift=LEFT * 2) for card in kw_cards],
            FadeOut(title, shift=UP),
            run_time=0.8
        )

        next_part = Text("Video sắp kết thúc — Tổng kết toàn bộ hành trình!",
                         font=FONT, font_size=28, color=WHITE)
        next_part.move_to(ORIGIN)
        self.play(FadeOut(summary_box), FadeOut(summary))
        self.play(FadeIn(next_part), run_time=1)
        self.wait(2)
        self.play(FadeOut(next_part))
