# scenes/part3_world_models.py — Trực: Phần 3: Mô hình thế giới cho robot (Sc32-44)
# Render toàn bộ: manim -pql scenes/part3_world_models.py -a
# Render 1 scene: manim -pql scenes/part3_world_models.py Scene32_Part3Intro
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


def make_white_title(text, sub=""):
    """
    Tạo VGroup tiêu đề chuẩn hóa với toàn bộ chữ màu trắng (WHITE).
    """
    title_obj = make_title(text, sub)
    if sub and isinstance(title_obj, VGroup):
        title_obj[1].set_color(WHITE)
    return title_obj

def make_checkmark(size=0.3, stroke_width=3, color=C_GREEN):
    """
    Tạo dấu tích (checkmark) tinh tế và chuyên nghiệp.
    """
    line1 = Line(LEFT * size * 0.4 + DOWN * size * 0.1, ORIGIN + DOWN * size * 0.35, color=color, stroke_width=stroke_width)
    line2 = Line(ORIGIN + DOWN * size * 0.35, RIGHT * size * 0.5 + UP * size * 0.35, color=color, stroke_width=stroke_width)
    return VGroup(line1, line2)

def make_premium_cross_badge(box, size=0.45):
    """
    Tạo một badge Failure cao cấp (vòng tròn mờ có dấu X đỏ) ở góc trên bên phải của hộp.
    """
    circle = Circle(radius=size/2, color=C_RED, fill_color=C_RED, fill_opacity=0.15, stroke_width=1.5)
    cross = make_cross(size=size*0.45, stroke_width=2.5, color=C_RED)
    badge = VGroup(circle, cross)
    badge.move_to(box.get_corner(UR) + LEFT * 0.35 + DOWN * 0.35)
    return badge


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 32 — Giới thiệu Phần 3                          ║
# ╚══════════════════════════════════════════════════════════╝
class Scene32_Part3Intro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Tiêu đề phần
        part_num = Text("PHẦN 3", font=FONT, font_size=56, color=WHITE)
        line1 = Text("Mở rộng mô hình thế giới", font=FONT, font_size=38, color=WHITE)
        line2 = Text("cho robot thông minh", font=FONT, font_size=38, color=WHITE)
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
        line = Line(LEFT * 5.5, RIGHT * 5.5, color=C_SUB, stroke_width=2).shift(UP * 0.6)
        self.play(Create(line))

        milestones = [
            ("2018", "World Models\n(Ha và Schmidhuber)", C_BLUE),
            ("2020", "Dreamer V1", C_PURPLE),
            ("2023", "Dreamer V3", C_YELLOW),
            ("2024-25", "Internet-scale\nWorld Models", C_GREEN),
        ]

        positions = [LEFT * 4.2, LEFT * 1.4, RIGHT * 1.4, RIGHT * 4.2]

        for i, ((year, desc, col), pos) in enumerate(zip(milestones, positions)):
            dot = Dot(point=pos + UP * 0.6, radius=0.12, color=col)
            y_label = Text(year, font=FONT, font_size=20, color=WHITE).next_to(dot, DOWN, buff=0.25)

            desc_lines = desc.split("\n")
            d_label = VGroup(*[
                Text(l, font=FONT, font_size=14, color=WHITE) for l in desc_lines
            ]).arrange(DOWN, buff=0.1).next_to(y_label, DOWN, buff=0.15)

            self.play(FadeIn(dot, scale=0.5), FadeIn(y_label), run_time=0.5)
            self.play(FadeIn(d_label, shift=UP * 0.2), run_time=0.4)

        # Mũi tên bước nhảy lớn
        jump_arrow = Arrow(
            RIGHT * 2.0 + DOWN * 0.3, RIGHT * 3.5 + DOWN * 0.3,
            color=C_YELLOW, stroke_width=3
        )
        jump_label = Text("Bước nhảy lớn!", font=FONT, font_size=16, color=WHITE)
        jump_label.next_to(jump_arrow, DOWN, buff=0.15)
        self.play(Create(jump_arrow), FadeIn(jump_label), run_time=0.6)

        # Thiết kế lại phần 2 yếu tố thành sự kết hợp Pill cao cấp
        pill1_box = RoundedRectangle(
            width=4.0, height=0.7, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.15, stroke_width=2
        )
        pill1_text = Text("Dữ liệu quy mô Internet", font=FONT, font_size=15, color=WHITE)
        pill1 = VGroup(pill1_box, pill1_text)

        plus_sign = Text("+", font=FONT, font_size=24, color=C_YELLOW)

        pill2_box = RoundedRectangle(
            width=4.0, height=0.7, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.15, stroke_width=2
        )
        pill2_text = Text("Kiến trúc mở rộng mạnh", font=FONT, font_size=15, color=WHITE)
        pill2 = VGroup(pill2_box, pill2_text)

        combo_row = VGroup(pill1, plus_sign, pill2).arrange(RIGHT, buff=0.35)
        combo_label = Text("Sự kết hợp đột phá tạo nên Internet-scale World Models:", font=FONT, font_size=16, color=WHITE)
        
        factor_group = VGroup(combo_label, combo_row).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.9)

        self.play(FadeIn(factor_group))
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

        # Con số ấn tượng - Trục dọc y = 1.2
        number_text = Text("21,000,000", font=FONT, font_size=72, color=C_YELLOW, weight=BOLD)
        number_text.move_to(UP * 1.2)
        
        # Nhãn phụ ngắn gọn và trực quan - Trục dọc y = 0.45
        sub_text = Text(
            "cặp dữ liệu Video - Hành động",
            font=FONT, font_size=24, color=WHITE
        ).next_to(number_text, DOWN, buff=0.25)

        self.play(FadeIn(number_text, scale=0.5), run_time=1)
        self.play(FadeIn(sub_text), run_time=0.6)
        self.wait(1)

        # "Time-Aligned" highlight - Rộng hơn, chi tiết hơn - Trục dọc y = -0.3
        aligned_box = RoundedRectangle(
            width=9.5, height=0.8, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.12, stroke_width=2
        ).shift(DOWN * 0.3)
        aligned_text = Text(
            "Căn chỉnh theo thời gian (Time-Aligned): Hành động khớp với từng frame",
            font=FONT, font_size=15, color=WHITE
        ).move_to(aligned_box)
        self.play(FadeIn(aligned_box), FadeIn(aligned_text), run_time=0.8)
        self.wait(0.5)

        core_idea = Text(
            "Video = Ngôn ngữ chung cho việc ra quyết định",
            font=FONT, font_size=24, color=WHITE
        ).to_edge(DOWN, buff=1.2)
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
            ("Text-Video", "Video + mô tả hành động", C_BLUE),
            ("Camera Control", "Video + thông tin xoay 360°", C_GREEN),
            ("Robot Control", "Video + vector vận tốc Δx, Δy", C_YELLOW),
            ("Keyboard Control", "Video game + lịch sử nhấn phím", C_PURPLE),
        ]

        cards = VGroup()
        for type_name, example, col in data_types:
            box = RoundedRectangle(
                width=2.8, height=1.6, corner_radius=0.12,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            name = Text(type_name, font=FONT, font_size=15, color=col, weight=BOLD)

            # Ví dụ - chia dòng và dùng chữ màu trắng toàn bộ
            ex_lines = example.split(" + ")
            ex_group = VGroup(*[
                Text(l, font=FONT, font_size=11, color=WHITE) for l in ex_lines
            ]).arrange(DOWN, buff=0.08)

            # Căn giữa nội dung chữ tuyệt đối cả dọc và ngang bên trong khung box
            card_content = VGroup(name, ex_group).arrange(DOWN, buff=0.18).move_to(box)
            cards.add(VGroup(box, card_content))

        cards.arrange(RIGHT, buff=0.25).shift(UP * 0.2)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.6)
            self.wait(0.3)

        conclusion = Text(
            "→ Sự đa dạng giúp mô hình học được quy luật vật lý tổng quát",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 36 — Action Conditioning: Thách thức              ║
# ╚══════════════════════════════════════════════════════════╝
class Scene36_ActionChallenge(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_white_title("Action Conditioning", "Đưa hành động robot vào mô hình video")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Câu hỏi trung tâm
        question = Text(
            "Thách thức: Làm sao đưa continuous action vào video diffusion model?",
            font=FONT, font_size=20, color=WHITE
        ).shift(UP * 1.4)
        self.play(FadeIn(question), run_time=0.8)
        self.wait(0.5)

        # Phương pháp sai 1: Discretization
        wrong1_box = RoundedRectangle(
            width=4.5, height=2.6, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        w1_title = Text("Discretization / Text Embedding", font=FONT, font_size=16, color=C_RED, weight=BOLD)
        w1_steps = VGroup(
            Text("Vector liên tục → Rời rạc hóa", font=FONT, font_size=14, color=WHITE),
            Text("hoặc Text encode (CLIP/T5)", font=FONT, font_size=14, color=WHITE),
            Text("Robot giật cục, sai lệch vị trí", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        w1_cross = make_cross(size=0.28, stroke_width=3, color=C_RED)
        w1_content = VGroup(w1_title, w1_steps, w1_cross).arrange(DOWN, buff=0.18).move_to(wrong1_box)
        wrong1_group = VGroup(wrong1_box, w1_content)

        # Phương pháp sai 2: Text embedding
        wrong2_box = RoundedRectangle(
            width=4.5, height=2.6, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        w2_title = Text("Text Embedding (TinyLlama/CLIP)", font=FONT, font_size=16, color=C_RED, weight=BOLD)
        w2_steps = VGroup(
            Text("Vector → Text encode → Mô hình", font=FONT, font_size=14, color=WHITE),
            Text("Vật lý bị drift hoàn toàn", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        w2_cross = make_cross(size=0.28, stroke_width=3, color=C_RED)
        w2_content = VGroup(w2_title, w2_steps, w2_cross).arrange(DOWN, buff=0.18).move_to(wrong2_box)
        wrong2_group = VGroup(wrong2_box, w2_content)

        # Sắp xếp 2 phương pháp sai đối xứng hoàn hảo
        wrong_pair = VGroup(wrong1_group, wrong2_group).arrange(RIGHT, buff=0.8).shift(DOWN * 0.2)

        # Trình diễn hiệu ứng xuất hiện tuần tự cực kỳ mượt mà
        self.play(FadeIn(wrong1_group, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeIn(wrong2_group, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        conclusion = Text(
            "→ Cả hai phương pháp đều làm robot di chuyển sai lệch nghiêm trọng!",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 37 — Action Conditioning: Linear Projection       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene37_LinearProjection(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Giải pháp: Linear Projection")
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.8)
        self.wait(0.3)

        # Khung màu cam lớn chứa cả công thức và định nghĩa
        middle_box = RoundedRectangle(
            width=11.2, height=3.0, corner_radius=0.15,
            color="#F97316", fill_opacity=0.08, stroke_width=1.5
        ).move_to(UP * 0.3)

        # --- BÊN TRÁI: Công thức chính ---
        formula_label = Text("Công thức chính", font=FONT, font_size=15, color="#F97316", weight=BOLD)
        formula = MathTex(
            r"\vec{h}_a", r"=", r"W", r"\cdot", r"\vec{a}",
            font_size=44, color=WHITE
        )
        
        formula_label.move_to(middle_box.get_left() + RIGHT * 2.8 + UP * 0.4)
        formula.move_to(middle_box.get_left() + RIGHT * 2.8 + DOWN * 0.3)

        # --- BÊN PHẢI: Giải thích biến ---
        # Gộp biến và dấu "=" vào cùng một MathTex để LaTeX tự căn baseline
        row_h = MathTex(r"\vec{h}_a", r"=", font_size=34, color=WHITE)
        row_W = MathTex(r"W", r"=", font_size=34, color=WHITE)
        row_a = MathTex(r"\vec{a}", r"=", font_size=34, color=WHITE)

        # Sắp xếp 3 hàng theo chiều dọc, căn lề theo dấu "=" (phần tử [1])
        rows = VGroup(row_h, row_W, row_a).arrange(DOWN, buff=0.45)
        # Căn thẳng cột dấu "=" theo chiều ngang
        for row in [row_W, row_a]:
            row[1].align_to(row_h[1], LEFT)
            row[0].align_to(row_h[0], RIGHT)

        # Nội dung chữ (chữ bé -> màu trắng)
        desc_h = Text("action feature → cộng vào latent space", font=FONT, font_size=15, color=WHITE)
        desc_W = Text("weight matrix (học được)", font=FONT, font_size=15, color=WHITE)
        desc_a = Text("raw action vector (vận tốc, lực)", font=FONT, font_size=15, color=WHITE)

        # Đặt text mô tả ngay sau dấu "=" của mỗi hàng
        desc_h.next_to(row_h[1], RIGHT, buff=0.25)
        desc_W.next_to(row_W[1], RIGHT, buff=0.25)
        desc_a.next_to(row_a[1], RIGHT, buff=0.25)

        desc_col = VGroup(desc_h, desc_W, desc_a)

        definitions = VGroup(rows, desc_col)
        definitions.move_to(middle_box.get_right() + LEFT * 3.3)

        # Hiện phần khung và tiêu đề trước
        self.play(
            FadeIn(middle_box, shift=UP * 0.2),
            FadeIn(formula_label, shift=RIGHT * 0.2),
            run_time=0.8
        )
        
        # Viết công thức chính bên trái
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)

        # Hiệu ứng nhân bản từng biến bay sang phải và hiện giải thích
        # 1. Nhân bản biến h_a
        clone_h = formula[0].copy()
        self.play(Transform(clone_h, row_h[0]), run_time=0.8)
        self.play(FadeIn(row_h[1]), FadeIn(desc_h), run_time=0.5)
        self.wait(0.3)

        # 2. Nhân bản biến W
        clone_W = formula[2].copy()
        self.play(Transform(clone_W, row_W[0]), run_time=0.8)
        self.play(FadeIn(row_W[1]), FadeIn(desc_W), run_time=0.5)
        self.wait(0.3)

        # 3. Nhân bản biến a
        clone_a = formula[4].copy()
        self.play(Transform(clone_a, row_a[0]), run_time=0.8)
        self.play(FadeIn(row_a[1]), FadeIn(desc_a), run_time=0.5)
        self.wait(0.5)

        # So sánh kết quả bên dưới
        compare_box_width = 5.2
        compare_box_height = 1.3

        # Box 1 (Trái - Discretization)
        bad_box = RoundedRectangle(
            width=compare_box_width, height=compare_box_height, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=1.5
        )
        bad_label = Text("Discretization", font=FONT, font_size=16, color=C_RED, weight=BOLD)
        bad_result_text = Text("Robot giật cục, sai lệch", font=FONT, font_size=14, color=WHITE)
        bad_content = VGroup(bad_label, bad_result_text).arrange(DOWN, buff=0.15).move_to(bad_box)
        bad_group = VGroup(bad_box, bad_content)

        # Box 2 (Phải - Linear Projection)
        good_box = RoundedRectangle(
            width=compare_box_width, height=compare_box_height, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.08, stroke_width=1.5
        )
        good_label = Text("Linear Projection", font=FONT, font_size=16, color=C_GREEN, weight=BOLD)
        good_result_text = Text("Robot mượt mà, chính xác", font=FONT, font_size=14, color=WHITE)
        good_content = VGroup(good_label, good_result_text).arrange(DOWN, buff=0.15).move_to(good_box)
        good_group = VGroup(good_box, good_content)

        compare = VGroup(bad_group, good_group).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(compare, shift=UP * 0.4), run_time=1.0)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 38 — Video Language Planning: Ý tưởng            ║
# ╚══════════════════════════════════════════════════════════╝
class Scene38_VLP_Idea(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Video Language Planning (VLP)", "Lập kế hoạch phân cấp cho robot")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)

        # Thẻ Nhiệm vụ (Màu xanh lam mờ)
        task_box = RoundedRectangle(
            width=9.2, height=1.1, corner_radius=0.15,
            color=C_BLUE, fill_opacity=0.08, stroke_width=1.5
        )
        task_label = Text("NHIỆM VỤ DÀI HẠN CỦA ROBOT", font=FONT, font_size=11, color=C_BLUE, weight=BOLD)
        task_text = Text(
            "\"Dọn dẹp bàn ăn và cất quả táo vào ngăn kéo\"",
            font=FONT, font_size=15, color=WHITE, weight=BOLD
        )
        task_content = VGroup(task_label, task_text).arrange(DOWN, buff=0.12).move_to(task_box)
        task_card = VGroup(task_box, task_content)

        # Thẻ Thách thức & Trở ngại (Màu đỏ mờ)
        problem_box = RoundedRectangle(
            width=9.2, height=1.6, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=1.5
        )
        problem_title = Text("THÁCH THỨC & TRỞ NGẠI", font=FONT, font_size=11, color=C_RED, weight=BOLD)
        
        problem_line1 = Text(
            "Hỏi: Làm sao sinh video dài thể hiện toàn bộ quá trình?",
            font=FONT, font_size=14, color=WHITE
        )
        problem_line2 = Text(
            "Đáp: Sinh video dài trong 1 lượt → suy giảm chất lượng nghiêm trọng!",
            font=FONT, font_size=14, color=WHITE
        )
        # Căn giữa phần Hỏi/Đáp
        problem_qa = VGroup(problem_line1, problem_line2).arrange(DOWN, aligned_edge=ORIGIN, buff=0.12)
        
        problem_content = VGroup(problem_title, problem_qa).arrange(DOWN, buff=0.18).move_to(problem_box)
        problem_card = VGroup(problem_box, problem_content)

        # Thẻ Giải pháp đột phá VLP (Màu xanh lá mờ - Viền dày nổi bật)
        solution_box = RoundedRectangle(
            width=9.2, height=1.1, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2.5
        )
        solution_label = Text("GIẢI PHÁP ĐỘT PHÁ (VLP)", font=FONT, font_size=11, color=C_GREEN, weight=BOLD)
        solution_text = Text(
            "Video Language Planning — Lập kế hoạch phân cấp kết hợp Ngôn ngữ + Video",
            font=FONT, font_size=14, color=WHITE, weight=BOLD
        )
        solution_content = VGroup(solution_label, solution_text).arrange(DOWN, buff=0.12).move_to(solution_box)
        solution_card = VGroup(solution_box, solution_content)

        # Sắp xếp dọc - dịch xuống thấp hơn tránh dính phụ đề
        cards = VGroup(task_card, problem_card, solution_card).arrange(DOWN, buff=0.35).shift(DOWN * 0.65)

        # Xuất hiện tuần tự, tạo điểm nhấn cho Giải pháp đột phá ở cuối
        self.play(FadeIn(task_card, shift=UP * 0.2), run_time=0.7)
        self.wait(0.2)
        self.play(FadeIn(problem_card, shift=UP * 0.2), run_time=0.7)
        self.wait(0.2)
        self.play(FadeIn(solution_card, scale=0.95), run_time=0.9)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 39 — VLP: 3 cấp chi tiết                         ║
# ╚══════════════════════════════════════════════════════════╝
class Scene39_VLP_ThreeLevels(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("VLP: Lập kế hoạch 3 cấp")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)

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
                width=8.5, height=1.6, corner_radius=0.15,
                color=col, fill_opacity=0.10, stroke_width=1.5
            )
            
            # Cột bên trái: Tên cấp độ (đậm, trùng màu khung) + mô tả ngắn màu trắng
            name_text = Text(level_name, font=FONT, font_size=18, color=col, weight=BOLD)
            desc_text = Text(level_desc, font=FONT, font_size=13, color=WHITE)
            left_col = VGroup(name_text, desc_text).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            left_col.align_to(box.get_left(), LEFT).shift(RIGHT * 0.5)
            
            # Cột bên phải: Các bước thực hiện chi tiết (căn lề trái, dịch lệch nhiều sang phải)
            ex_lines = example.split("\n")
            ex_group = VGroup(*[
                Text(l, font=FONT, font_size=12, color=WHITE) for l in ex_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            ex_group.align_to(box.get_left(), LEFT).shift(RIGHT * 5.2)
            
            # Căn giữa hoàn toàn theo chiều dọc và chiều ngang bên trong khung
            left_col.set_y(box.get_y())
            ex_group.set_y(box.get_y())
            
            level_groups.add(VGroup(box, left_col, ex_group))

        # Căn giữa lại 3 khung trên màn hình
        level_groups.arrange(DOWN, buff=0.2).shift(DOWN * 0.3)

        # Mũi tên nối mượt mà giữa các cấp
        arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                level_groups[i][0].get_bottom(), level_groups[i + 1][0].get_top(),
                color=C_TEXT_SUB, stroke_width=1.5, buff=0.05,
                max_tip_length_to_length_ratio=0.25
            )
            arrows.add(arr)

        for i, lg in enumerate(level_groups):
            self.play(FadeIn(lg, shift=RIGHT * 0.3), run_time=0.7)
            if i < 2:
                self.play(Create(arrows[i]), run_time=0.3)
            self.wait(0.2)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 40 — Đánh giá Robot: Vấn đề                      ║
# ╚══════════════════════════════════════════════════════════╝
class Scene40_EvalProblem(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Đánh giá Robot Policy", "Vấn đề của phương pháp cũ")
        title[1].set_color(WHITE) # Đổi màu phụ đề thành màu trắng
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)

        # Phương pháp 1: Robot thật
        real_box = RoundedRectangle(
            width=4.4, height=2.0, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=1.5
        )
        real_icon = Text("🤖", font_size=32)
        real_title = Text("Robot thật", font=FONT, font_size=18, color=C_RED, weight=BOLD)
        real_header = VGroup(real_icon, real_title).arrange(RIGHT, buff=0.15)
        
        real_issues = VGroup(
            Text("• Cực kỳ đắt đỏ ($$$)", font=FONT, font_size=14, color=WHITE),
            Text("• Robot có thể bị hỏng", font=FONT, font_size=14, color=WHITE),
            Text("• Tốn thời gian vận hành", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        
        real_content = VGroup(real_header, real_issues).arrange(DOWN, buff=0.18).move_to(real_box)
        real_card = VGroup(real_box, real_content)

        # Phương pháp 2: Simulator truyền thống
        sim_box = RoundedRectangle(
            width=4.4, height=2.0, corner_radius=0.15,
            color=C_RED, fill_opacity=0.08, stroke_width=1.5
        )
        sim_icon = Text("💻", font_size=32)
        sim_title = Text("Simulator truyền thống", font=FONT, font_size=18, color=C_RED, weight=BOLD)
        sim_header = VGroup(sim_icon, sim_title).arrange(RIGHT, buff=0.15)
        
        sim_issues = VGroup(
            Text("• Sim-to-real gap quá lớn", font=FONT, font_size=14, color=WHITE),
            Text("• Kết quả không tương quan thực tế", font=FONT, font_size=14, color=WHITE),
            Text("• Vật lý mô phỏng quá đơn giản", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        
        sim_content = VGroup(sim_header, sim_issues).arrange(DOWN, buff=0.18).move_to(sim_box)
        sim_card = VGroup(sim_box, sim_content)

        # Sắp xếp hai box nằm ngang hàng
        pair = VGroup(real_card, sim_card).arrange(RIGHT, buff=0.8).shift(DOWN * 0.1)

        # Hiện từng box
        self.play(FadeIn(real_card, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(sim_card, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        conclusion = Text(
            "→ Cần phương pháp đánh giá mới: rẻ, nhanh, sát thực tế!",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 41 — Đánh giá Robot: Dùng Mô hình Thế giới       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene41_EvalWorldModel(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Đánh giá bằng Mô hình Thế giới")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)

        # Pipeline: Robot Policy → World Model → Video → VLM → Score
        steps = [
            ("Robot Policy", C_BLUE),
            ("World Model", C_GREEN),
            ("Video giả lập", C_YELLOW),
            ("VLM (chấm điểm)", C_PURPLE),
            ("Score ✓/✗", C_RED),
        ]

        step_boxes = VGroup()
        for step_name, col in steps:
            # Thiết kế node dẹt nằm ngang, chữ viết trên 1 dòng trùng màu viền
            box = RoundedRectangle(
                width=2.4, height=0.6, corner_radius=0.12,
                color=col, fill_opacity=0.08, stroke_width=1.5
            )
            label = Text(step_name, font=FONT, font_size=11, color=col, weight=BOLD).move_to(box)
            step_boxes.add(VGroup(box, label))

        step_boxes.arrange(RIGHT, buff=0.3).shift(UP * 0.5)

        # Trình diễn hiệu ứng xuất hiện chuỗi Pipeline kèm mũi tên sắc nét
        self.play(FadeIn(step_boxes[0], scale=0.85), run_time=0.5)
        for i in range(1, len(step_boxes)):
            arr = Arrow(
                step_boxes[i - 1][0].get_right(), step_boxes[i][0].get_left(),
                color=C_TEXT_SUB, stroke_width=2.5, buff=0.08,
                max_tip_length_to_length_ratio=0.25
            )
            self.play(
                Create(arr),
                FadeIn(step_boxes[i], shift=LEFT * 0.2),
                run_time=0.4
            )

        self.wait(0.5)

        # Thẻ giải thích tích hợp ở dưới đáy (màu xanh lá mờ, nhỏ gọn hơn)
        explain_box = RoundedRectangle(
            width=11.2, height=1.1, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.08, stroke_width=1.5
        ).to_edge(DOWN, buff=1.3) # Đẩy card lên cao hơn
        
        explain_title = Text("Ý NGHĨA CỦA PHƯƠNG PHÁP", font=FONT, font_size=12, color=C_GREEN, weight=BOLD)
        
        explain_line1 = Text(
            "• World Model đóng vai trò bộ giả lập học máy: Sinh video từ hành động của robot",
            font=FONT, font_size=13, color=WHITE
        )
        explain_line2 = Text(
            "• VLM đóng vai trò giám khảo: Đánh giá nhiệm vụ thành công/thất bại trực tiếp trên video",
            font=FONT, font_size=13, color=WHITE
        )
        explain_line3 = Text(
            "→ Đánh giá tự động hoàn toàn, không cần robot thật, loại bỏ sim-to-real gap!",
            font=FONT, font_size=16, color=C_GREEN, weight=BOLD
        )
        
        # Sắp xếp hai dòng giải thích trong card
        explain_lines = VGroup(explain_line1, explain_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        explain_content = VGroup(explain_title, explain_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Căn giữa hoàn hảo theo chiều dọc, căn lề trái thụt lề RIGHT*0.6
        explain_content.move_to(explain_box)
        explain_content.align_to(explain_box, LEFT).shift(RIGHT * 0.6)
        
        # Dòng 3 đặt bên ngoài khung, căn giữa màn hình
        explain_line3.next_to(explain_box, DOWN, buff=0.35)
        
        explain_group = VGroup(explain_box, explain_content)

        self.play(FadeIn(explain_box, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(explain_title, shift=RIGHT * 0.2), run_time=0.4)
        for line in explain_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.1)
        
        self.play(FadeIn(explain_line3, shift=UP * 0.2), run_time=0.6)

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
            width=4.5, height=2.6, corner_radius=0.15,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=2
        )
        fn_title = Text("False Negative", font=FONT, font_size=18, color=C_YELLOW, weight=BOLD)
        fn_steps = VGroup(
            Text("Robot hành động ĐÚNG ✓", font=FONT, font_size=14, color=WHITE, t2c={"ĐÚNG ✓": C_GREEN}),
            Text("↓", font_size=18, color=WHITE),
            Text("World Model render video lỗi", font=FONT, font_size=14, color=WHITE),
            Text("↓", font_size=18, color=WHITE),
            Text("VLM đánh giá: THẤT BẠI ✗", font=FONT, font_size=14, color=WHITE, t2c={"THẤT BẠI ✗": C_RED}),
        ).arrange(DOWN, buff=0.08)
        fn_content = VGroup(fn_title, fn_steps).arrange(DOWN, buff=0.18).move_to(fn_box)
        fn_group = VGroup(fn_box, fn_content)

        # === FALSE POSITIVE ===
        fp_box = RoundedRectangle(
            width=4.5, height=2.6, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.08, stroke_width=2
        )
        fp_title = Text("False Positive", font=FONT, font_size=18, color=C_PURPLE, weight=BOLD)
        fp_steps = VGroup(
            Text("Robot hành động SAI ✗", font=FONT, font_size=14, color=WHITE, t2c={"SAI ✗": C_RED}),
            Text("↓", font_size=18, color=WHITE),
            Text("World Model tự \"sửa sai\" video", font=FONT, font_size=14, color=WHITE),
            Text("↓", font_size=18, color=WHITE),
            Text("VLM đánh giá: THÀNH CÔNG ✓", font=FONT, font_size=14, color=WHITE, t2c={"THÀNH CÔNG ✓": C_GREEN}),
        ).arrange(DOWN, buff=0.08)
        fp_content = VGroup(fp_title, fp_steps).arrange(DOWN, buff=0.18).move_to(fp_box)
        fp_group = VGroup(fp_box, fp_content)

        errors = VGroup(fn_group, fp_group).arrange(RIGHT, buff=0.6).shift(UP * 0.1)

        # Animate
        self.play(FadeIn(fn_group, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(1)
        self.play(FadeIn(fp_group, shift=LEFT * 0.3), run_time=0.8)
        self.wait(0.5)

        warning = Text(
            "→ Cả hai lỗi đều nguy hiểm, cần cơ chế tự cải tiến!",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(warning))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 43 — Vòng lặp tự cải tiến                        ║
# ╚══════════════════════════════════════════════════════════╝
class Scene43_SelfImproving(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vòng lặp tự cải tiến")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # Trung tâm: World Model
        center_box = RoundedRectangle(
            width=3.5, height=1.5, corner_radius=0.2,
            color=C_GREEN, fill_opacity=0.15, stroke_width=2
        ).move_to(ORIGIN)
        center_label = Text("World Model", font=FONT, font_size=22, color=C_GREEN, weight=BOLD)
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
        ).arrange(DOWN, buff=0.45).move_to(LEFT * 4 + DOWN * 0.2)

        for step in ai_steps:
            step[1].set_color(C_BLUE)
            step[1].set_font_size(15)

        ai_arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                ai_steps[i].get_bottom(), ai_steps[i + 1].get_top(),
                color=C_BLUE, stroke_width=1.5, buff=0.05,
                max_tip_length_to_length_ratio=0.3
            )
            ai_arrows.add(arr)

        # Mũi tên từ World Model sang bước đầu tiên
        ai_start = Arrow(
            center_box.get_left(), ai_steps[0].get_right(),
            color=C_BLUE, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        # Mũi tên từ DPO về World Model
        ai_return = Arrow(
            ai_steps[2].get_right(), center_box.get_left(),
            color=C_BLUE, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(FadeIn(ai_title), run_time=0.5)
        self.play(Create(ai_start), run_time=0.4)
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
        ).arrange(DOWN, buff=0.45).move_to(RIGHT * 4 + DOWN * 0.2)

        for step in exec_steps:
            step[1].set_color(C_YELLOW)
            step[1].set_font_size(15)

        exec_arrows = VGroup()
        for i in range(2):
            arr = Arrow(
                exec_steps[i].get_bottom(), exec_steps[i + 1].get_top(),
                color=C_YELLOW, stroke_width=1.5, buff=0.05,
                max_tip_length_to_length_ratio=0.3
            )
            exec_arrows.add(arr)

        # Mũi tên từ World Model sang bước đầu tiên
        exec_start = Arrow(
            center_box.get_right(), exec_steps[0].get_left(),
            color=C_YELLOW, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        # Mũi tên từ DAgger về World Model
        exec_return = Arrow(
            exec_steps[2].get_left(), center_box.get_right(),
            color=C_YELLOW, stroke_width=2, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(FadeIn(exec_title), run_time=0.5)
        self.play(Create(exec_start), run_time=0.4)
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

        title = make_title("Tổng kết phần 3")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 3 bullet points recap (tất cả màu trắng, công thức MathTex có subscript)
        bullet1 = Text("• Dữ liệu quy mô lớn: 21 triệu cặp time-aligned data", font=FONT, font_size=18, color=WHITE)
        
        bullet2_text = Text("• Action Conditioning: Linear Projection (", font=FONT, font_size=18, color=WHITE)
        bullet2_formula = MathTex(r"h_a = W \cdot a", font_size=22, color=WHITE)
        bullet2_end = Text(")", font=FONT, font_size=18, color=WHITE)
        
        bullet2_formula.next_to(bullet2_text, RIGHT, buff=0.06)
        bullet2_formula.align_to(bullet2_text, DOWN).shift(UP * 0.04)
        bullet2_end.next_to(bullet2_formula, RIGHT, buff=0.06)
        bullet2_end.align_to(bullet2_text, DOWN)
        
        bullet2 = VGroup(bullet2_text, bullet2_formula, bullet2_end)
        
        bullet3 = Text("• Tự cải tiến: AI Feedback + Execution Feedback", font=FONT, font_size=18, color=WHITE)

        bullets = VGroup(bullet1, bullet2, bullet3).arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(UP * 0.5)

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)

        self.wait(1)

        # Sơ đồ tổng hợp nhỏ ở dưới - Nâng cao lên cho cân đối
        summary_box = RoundedRectangle(
            width=10, height=1.5, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.9)

        summary = VGroup(
            Text("VLP giúp robot thực hiện nhiệm vụ dài hạn", font=FONT, font_size=18, color=WHITE),
            Text("World Model đóng vai trò bộ giả lập để đánh giá robot policy", font=FONT, font_size=18, color=WHITE),
        ).arrange(DOWN, buff=0.15).move_to(summary_box)

        self.play(FadeIn(summary_box), FadeIn(summary), run_time=1)
        self.wait(2)

        # Transition
        self.play(
            FadeOut(bullets, shift=LEFT * 2),
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
