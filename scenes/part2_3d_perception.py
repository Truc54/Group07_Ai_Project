# scenes/part2_3d_perception.py — Tuấn: Phần 2: Nhận thức 3D liên tục (Sc18-31)
# Render toàn bộ: manim -pql scenes/part2_3d_perception.py -a
# Render 1 scene: manim -pql scenes/part2_3d_perception.py Scene18_Part2Intro
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 18 — Giới thiệu Phần 2 (~40s)                   ║
# ╚══════════════════════════════════════════════════════════╝
class Scene18_Part2Intro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # === Tiêu đề phần ===
        part_num = Text("PHẦN 2", font=FONT, font_size=56, color=WHITE)
        line1 = Text("Nhận thức 3D liên tục", font=FONT, font_size=38, color=WHITE)
        line2 = Text("từ video", font=FONT, font_size=38, color=WHITE)
        part_title = VGroup(line1, line2).arrange(DOWN, buff=0.2)
        part_group = VGroup(part_num, part_title).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(part_num, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(part_title), run_time=1.2)
        self.wait(1)

        # === Transformation: 2D → 3D ===
        self.play(FadeOut(part_group))

        # 2D plane
        plane_2d = Rectangle(width=2.5, height=2.0, color=C_RED, fill_opacity=0.15, stroke_width=2)
        label_2d = Text("2D Pixels", font=FONT, font_size=18, color=WHITE)
        label_2d.move_to(plane_2d)
        group_2d = VGroup(plane_2d, label_2d).shift(LEFT * 3.5)

        # Arrow transform
        transform_arrow = Arrow(
            LEFT * 2, RIGHT * 2,
            color=C_YELLOW, stroke_width=3
        )
        transform_label = Text("Understanding", font=FONT, font_size=16, color=C_YELLOW, weight=BOLD)
        transform_label.next_to(transform_arrow, UP, buff=0.15)

        # 3D cube
        cube_3d = Prism(
            dimensions=[2.5, 2.0, 1.5],
            fill_opacity=0.15, fill_color=C_GREEN,
            stroke_width=2, stroke_color=C_GREEN
        )
        label_3d = Text("3D Structure", font=FONT, font_size=18, color=WHITE)
        label_3d.move_to(cube_3d)
        group_3d = VGroup(cube_3d, label_3d).shift(RIGHT * 3.5)

        self.play(
            FadeIn(group_2d, shift=LEFT * 0.2),
            FadeIn(transform_arrow),
            FadeIn(transform_label),
            FadeIn(group_3d, shift=RIGHT * 0.2),
            run_time=1.2
        )
        self.wait(1)

        # === Mô tả phần ===
        description = Text(
            "Xây dựng mô hình AI hiểu cấu trúc không gian 3 chiều từ luồng video liên tục",
            font=FONT, font_size=18, color=C_SUB
        ).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(description, shift=UP * 0.3), run_time=0.8)
        self.wait(2)

        # === Transition ===
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 19 — Phê phán: Video đẹp nhưng rỗng (~50s)       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene19_PixelOnlyCritique(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vấn đề: Video đẹp nhưng rỗng")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === BÊN TRÁI: Bề ngoài đẹp ===
        left_box = RoundedRectangle(
            width=4.0, height=2.2, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        )
        left_icon = Text("✨", font_size=40)
        left_title = Text("Bề ngoài", font=FONT, font_size=18, color=C_GREEN, weight=BOLD)
        left_items = VGroup(
            Text("• Sóng nước lấp lánh", font=FONT, font_size=12, color=WHITE),
            Text("• Phản chiếu ánh sáng", font=FONT, font_size=12, color=WHITE),
            Text("• Bóng đổ chân thực", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        left_content = VGroup(left_icon, left_title, left_items).arrange(DOWN, buff=0.18).move_to(left_box)
        left_group = VGroup(left_box, left_content)
        left_group.shift(LEFT * 4.2 + UP * 0.3)

        # === BÊN PHẢI: Bên trong rỗng ===
        right_box = RoundedRectangle(
            width=4.0, height=2.2, corner_radius=0.12,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        right_icon = Text("∅", font_size=40)
        right_title = Text("Bên trong", font=FONT, font_size=18, color=C_RED, weight=BOLD)
        right_desc = VGroup(
            Text("Chỉ là pixel", font=FONT, font_size=12, color=WHITE),
            Text("renderer siêu việt", font=FONT, font_size=12, color=WHITE),
            Text("Không có 3D", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        right_content = VGroup(right_icon, right_title, right_desc).arrange(DOWN, buff=0.18).move_to(right_box)
        right_group = VGroup(right_box, right_content)
        right_group.shift(RIGHT * 4.2 + UP * 0.3)

        # === Mũi tên "tách ra" ===
        split_arrow_left = Arrow(
            ORIGIN + LEFT * 0.8, ORIGIN + LEFT * 2.5,
            color=C_YELLOW, stroke_width=2
        )
        split_arrow_right = Arrow(
            ORIGIN + RIGHT * 0.8, ORIGIN + RIGHT * 2.5,
            color=C_YELLOW, stroke_width=2
        )

        self.play(
            FadeIn(left_group, shift=LEFT * 0.3),
            FadeIn(right_group, shift=RIGHT * 0.3),
            Create(split_arrow_left),
            Create(split_arrow_right),
            run_time=1.2
        )
        self.wait(1)

        # === Kết luận ===
        conclusion = Text(
            "→ Mô hình học cách phân phối pixel trên mặt phẳng 2D, nhưng không có structured 3D representation",
            font=FONT, font_size=16, color=C_RED
        ).to_edge(DOWN, buff=1.0)

        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 20 — Khi góc quay thay đổi (~50s)               ║
# ╚══════════════════════════════════════════════════════════╝
class Scene20_StructuralDrift(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vấn đề: Structural Drift & Morphing")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Vấn đề 1: Structural Drift ===
        problem1_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.12,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        )
        p1_icon = Text("🔄", font_size=32)
        p1_title = Text("Structural Drift", font=FONT, font_size=16, color=C_RED, weight=BOLD)
        p1_desc = VGroup(
            Text("Vật thể quay → mặt sau", font=FONT, font_size=12, color=WHITE),
            Text("không được ghi nhớ", font=FONT, font_size=12, color=WHITE),
            Text("Hình dạng tự thay đổi", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.10)
        
        p1_content = VGroup(p1_icon, p1_title, p1_desc).arrange(DOWN, buff=0.15).move_to(problem1_box)
        p1_group = VGroup(problem1_box, p1_content)
        p1_group.shift(LEFT * 4.2 + DOWN * 0.3)

        # === Vấn đề 2: Morphing ===
        problem2_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.12,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=2
        )
        p2_icon = Text("👻", font_size=32)
        p2_title = Text("Morphing", font=FONT, font_size=16, color=C_YELLOW, weight=BOLD)
        p2_desc = VGroup(
            Text("Vật bị che khuất", font=FONT, font_size=12, color=WHITE),
            Text("Xuất hiện lại → bị biến", font=FONT, font_size=12, color=WHITE),
            Text("dạo hình dáng phi vật lý", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.10)
        
        p2_content = VGroup(p2_icon, p2_title, p2_desc).arrange(DOWN, buff=0.15).move_to(problem2_box)
        p2_group = VGroup(problem2_box, p2_content)
        p2_group.shift(RIGHT * 4.2 + DOWN * 0.3)

        # === Minh họa góc quay ===
        arrow_up = Arrow(
            DOWN * 0.5, UP * 0.5,
            color=C_BLUE, stroke_width=2
        )
        angle_label = Text("Góc quay thay đổi", font=FONT, font_size=14, color=C_BLUE)
        angle_label.next_to(arrow_up, LEFT, buff=0.2)

        self.play(
            FadeIn(p1_group, shift=LEFT * 0.3),
            FadeIn(p2_group, shift=RIGHT * 0.3),
            Create(arrow_up),
            FadeIn(angle_label),
            run_time=1.2
        )
        self.wait(1)

        # === Kết luận ===
        conclusion = Text(
            "→ Mô hình không có bộ nhớ vật lý để tái dựng cấu trúc",
            font=FONT, font_size=18, color=WHITE
        ).to_edge(DOWN, buff=1.0)

        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 21 — Streaming Perception: Ý tưởng (~50s)       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene21_StreamingPerceptionIdea(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Giải pháp: Streaming Perception")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Ví dụ: Trẻ sơ sinh ===
        baby_box = RoundedRectangle(
            width=4.5, height=1.8, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        )
        baby_icon = Text("👶", font_size=40)
        baby_desc = VGroup(
            Text("Trẻ sơ sinh lớn lên", font=FONT, font_size=14, color=WHITE, weight=BOLD),
            Text("Liên tục quan sát & xây dựng mô hình 3D trong đầu", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        baby_content = VGroup(baby_icon, baby_desc).arrange(DOWN, buff=0.18).move_to(baby_box)
        baby_group = VGroup(baby_box, baby_content)
        baby_group.shift(UP * 0.8)

        # === Ví dụ: Con người đi bộ ===
        human_box = RoundedRectangle(
            width=4.5, height=1.8, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        )
        human_icon = Text("🚶", font_size=40)
        human_desc = VGroup(
            Text("Đi bộ trong phòng", font=FONT, font_size=14, color=WHITE, weight=BOLD),
            Text("Não bộ liên tục cập nhật mô hình 3D bền vững", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        human_content = VGroup(human_icon, human_desc).arrange(DOWN, buff=0.18).move_to(human_box)
        human_group = VGroup(human_box, human_content)
        human_group.shift(DOWN * 0.8)

        # === Mũi tên chỉ AI ===
        ai_arrow = Arrow(
            RIGHT * 2.5 + UP * 0.8, RIGHT * 4.0 + UP * 0.8,
            color=C_YELLOW, stroke_width=2
        )
        ai_label = Text("AI cũng phải\nhoạt động tương tự", font=FONT, font_size=13, color=C_YELLOW)
        ai_label.next_to(ai_arrow, RIGHT, buff=0.2)

        self.play(
            FadeIn(baby_group, shift=UP * 0.2),
            FadeIn(human_group, shift=DOWN * 0.2),
            run_time=1.0
        )
        self.wait(0.5)

        self.play(
            Create(ai_arrow),
            FadeIn(ai_label),
            run_time=0.8
        )
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 22 — CUT3R: Giới thiệu (~45s)                   ║
# ╚══════════════════════════════════════════════════════════╝
class Scene22_CUT3RIntro(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("CUT3R", "Continuous Updating Transformer for 3D Reconstruction")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Đặc điểm CUT3R ===
        features = [
            ("Stateful Recurrent", "Duy trì trạng thái bộ nhớ", C_BLUE),
            ("Real-time Processing", "Không xử lý độc lập", C_GREEN),
            ("3D Memory State", "Giữ bộ nhớ 3D liên tục", C_YELLOW),
        ]

        cards = VGroup()
        for feature_name, feature_desc, col in features:
            box = RoundedRectangle(
                width=3.0, height=1.6, corner_radius=0.12,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            
            fname = Text(feature_name, font=FONT, font_size=15, color=col, weight=BOLD)
            fdesc = Text(feature_desc, font=FONT, font_size=12, color=WHITE)
            
            content = VGroup(fname, fdesc).arrange(DOWN, buff=0.15).move_to(box)
            cards.add(VGroup(box, content))

        cards.arrange(RIGHT, buff=0.4).shift(UP * 0.3)

        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
            self.wait(0.3)

        # === Core idea ===
        core_box = RoundedRectangle(
            width=9.0, height=1.0, corner_radius=0.12,
            color=C_PURPLE, fill_opacity=0.08, stroke_width=2
        ).to_edge(DOWN, buff=1.0)

        core_text = Text(
            "Camera → Transformer → 3D Memory State (được cập nhật liên tục)",
            font=FONT, font_size=15, color=WHITE
        ).move_to(core_box)

        self.play(FadeIn(core_box), FadeIn(core_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 23 — CUT3R: Quy trình cập nhật (~60s)            ║
# ╚══════════════════════════════════════════════════════════╝
class Scene23_CUT3RProcess(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("CUT3R: Quy trình cập nhật")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Layout: Hàng ngang dài ===
        # Input 1: S(t-1)
        mem_box = RoundedRectangle(
            width=1.6, height=1.2, corner_radius=0.10,
            color=C_BLUE, fill_opacity=0.15, stroke_width=2
        )
        mem_label_main = Text("S(t-1)", font=FONT, font_size=14, color=WHITE, weight=BOLD)
        mem_label_sub = Text("Bộ nhớ cũ", font=FONT, font_size=10, color=C_BLUE)
        mem_content = VGroup(mem_label_main, mem_label_sub).arrange(DOWN, buff=0.06).move_to(mem_box)
        mem_group = VGroup(mem_box, mem_content)

        # Input 2: I(t)
        frame_box = RoundedRectangle(
            width=1.6, height=1.2, corner_radius=0.10,
            color=C_GREEN, fill_opacity=0.15, stroke_width=2
        )
        frame_label_main = Text("I(t)", font=FONT, font_size=14, color=WHITE, weight=BOLD)
        frame_label_sub = Text("Khung mới", font=FONT, font_size=10, color=C_GREEN)
        frame_content = VGroup(frame_label_main, frame_label_sub).arrange(DOWN, buff=0.06).move_to(frame_box)
        frame_group = VGroup(frame_box, frame_content)

        # Sắp xếp 2 input theo chiều dọc để tránh mũi tên từ S(t-1) đi xuyên qua I(t)
        inputs = VGroup(mem_group, frame_group).arrange(DOWN, buff=0.5)

        # Transformer center
        trans_box = RoundedRectangle(
            width=2.2, height=1.4, corner_radius=0.12,
            color=C_YELLOW, fill_opacity=0.12, stroke_width=2
        )
        trans_title = Text("Transformer", font=FONT, font_size=12, color=WHITE, weight=BOLD)
        trans_op = Text("Update", font=FONT, font_size=11, color=WHITE)
        trans_content = VGroup(trans_title, trans_op).arrange(DOWN, buff=0.12).move_to(trans_box)
        trans_group = VGroup(trans_box, trans_content)

        # Output: S(t)
        out_box = RoundedRectangle(
            width=1.6, height=1.2, corner_radius=0.10,
            color=C_RED, fill_opacity=0.15, stroke_width=2
        )
        out_label_main = Text("S(t)", font=FONT, font_size=14, color=WHITE, weight=BOLD)
        out_label_sub = Text("Bộ nhớ mới", font=FONT, font_size=10, color=C_RED)
        out_content = VGroup(out_label_main, out_label_sub).arrange(DOWN, buff=0.06).move_to(out_box)
        out_group = VGroup(out_box, out_content)

        # === Sắp xếp toàn bộ thành hàng ngang ===
        # Input phía bên trái
        inputs.shift(LEFT * 4.5)
        
        # Transformer ở giữa
        trans_group.move_to(ORIGIN)
        
        # Output phía bên phải
        out_group.shift(RIGHT * 4.5)

        # === Arrows (sạch, không chồng) ===
        # Từ S(t-1) → Transformer
        arrow1 = Arrow(
            mem_group.get_right(),
            trans_box.get_left() + UP * 0.3,
            color=C_BLUE, stroke_width=2.5, buff=0.1
        )
        
        # Từ I(t) → Transformer
        arrow2 = Arrow(
            frame_group.get_right(),
            trans_box.get_left() + DOWN * 0.3,
            color=C_GREEN, stroke_width=2.5, buff=0.1
        )

        # Từ Transformer → S(t)
        arrow_out = Arrow(
            trans_box.get_right(),
            out_group.get_left(),
            color=C_RED, stroke_width=2.5, buff=0.1
        )

        # === Animate ===
        self.play(
            FadeIn(mem_group, shift=LEFT * 0.2),
            FadeIn(frame_group, shift=LEFT * 0.2),
            run_time=0.7
        )
        self.wait(0.3)

        self.play(
            Create(arrow1),
            Create(arrow2),
            run_time=0.6
        )
        self.wait(0.2)

        self.play(
            FadeIn(trans_group),
            run_time=0.6
        )
        self.wait(0.3)

        self.play(
            Create(arrow_out),
            FadeIn(out_group, shift=RIGHT * 0.2),
            run_time=0.8
        )
        self.wait(1)

        # === Khung tổng hợp ===
        full_pipeline = VGroup(
            inputs, arrow1, arrow2, trans_group, arrow_out, out_group
        )
        
        pipeline_box = SurroundingRectangle(
            full_pipeline,
            color=C_SUB, buff=0.3, stroke_width=2
        )

        self.play(Create(pipeline_box), run_time=0.6)
        self.wait(0.5)

        # === Loop label ===
        loop_label = Text(
            "Lặp lại mỗi khung hình",
            font=FONT, font_size=13, color=C_PURPLE, weight=BOLD
        ).next_to(pipeline_box, DOWN, buff=0.4)

        self.play(FadeIn(loop_label, shift=UP * 0.2), run_time=0.6)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 24 — CUT3R: Công thức (~45s)                    ║
# ╚══════════════════════════════════════════════════════════╝
class Scene24_CUT3RFormula(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("CUT3R: Công thức cập nhật")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Công thức chính ===
        formula_eq = MathTex(
            r"S_t = \text{TransformerUpdate}(S_{t-1}, I_t)",
            font_size=56, color=WHITE
        ).shift(UP * 1.0)

        self.play(Write(formula_eq), run_time=1.2)
        self.wait(1)

        # === Giải thích các thành phần ===
        explain_box = RoundedRectangle(
            width=9.5, height=1.8, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        ).shift(DOWN * 1.2)

        explain_lines = VGroup(
            Text("• S_t: Trạng thái bộ nhớ tại thời điểm t", font=FONT, font_size=14, color=WHITE),
            Text("• S_{t-1}: Bộ nhớ từ bước thời gian trước", font=FONT, font_size=14, color=WHITE),
            Text("• I_t: Khung hình video tại thời điểm t", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        
        explain_lines.move_to(explain_box).shift(LEFT * 0.3)

        self.play(FadeIn(explain_box), run_time=0.5)
        for line in explain_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)

        # === Highlight: Real-time ===
        realtime_box = RoundedRectangle(
            width=7.0, height=0.8, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.5)

        realtime_text = Text(
            "Thời gian thực: Mỗi khung chỉ mất vài mili-giây (không cần global optimization)",
            font=FONT, font_size=14, color=C_GREEN, weight=BOLD
        ).move_to(realtime_box)

        self.play(FadeIn(realtime_box), FadeIn(realtime_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 25 — CUT3R: Xử lý che khuất (~50s)              ║
# ╚══════════════════════════════════════════════════════════╝
class Scene25_CUT3ROcclusion(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("CUT3R: Xử lý vật thể bị che khuất")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === 3 bước ===
        
        # Bước 1: Camera thấy bàn
        step1_box = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        )
        step1_num = Text("①", font_size=32, color=C_BLUE)
        step1_text = Text("Camera thấy bàn\n→ Bộ nhớ lưu", font=FONT, font_size=13, color=WHITE, line_spacing=1.2)
        step1_content = VGroup(step1_num, step1_text).arrange(DOWN, buff=0.2).move_to(step1_box)
        step1_group = VGroup(step1_box, step1_content)

        # Bước 2: Camera quay đi
        step2_box = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.12,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=2
        )
        step2_num = Text("②", font_size=32, color=C_YELLOW)
        step2_text = Text("Camera quay đi\n→ Bộ nhớ giữ nguyên", font=FONT, font_size=13, color=WHITE, line_spacing=1.2)
        step2_content = VGroup(step2_num, step2_text).arrange(DOWN, buff=0.2).move_to(step2_box)
        step2_group = VGroup(step2_box, step2_content)

        # Bước 3: Camera quay lại
        step3_box = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        )
        step3_num = Text("③", font_size=32, color=C_GREEN)
        step3_text = Text("Camera quay lại\n→ Bàn tái hiện ✓", font=FONT, font_size=13, color=WHITE, line_spacing=1.2)
        step3_content = VGroup(step3_num, step3_text).arrange(DOWN, buff=0.2).move_to(step3_box)
        step3_group = VGroup(step3_box, step3_content)

        # Arrange steps
        steps = VGroup(step1_group, step2_group, step3_group).arrange(RIGHT, buff=0.5).shift(UP * 0.5)

        # Arrows between steps
        arrow1 = Arrow(
            step1_group.get_right(), step2_group.get_left(),
            color=C_SUB, stroke_width=2, buff=0.1
        )
        arrow2 = Arrow(
            step2_group.get_right(), step3_group.get_left(),
            color=C_SUB, stroke_width=2, buff=0.1
        )

        # Animate
        for i, step in enumerate(steps):
            self.play(FadeIn(step, shift=UP * 0.2), run_time=0.5)
            if i < 2:
                self.play(Create([arrow1, arrow2][i]), run_time=0.3)
            self.wait(0.3)

        # === Highlight ===
        highlight = Text(
            "✓ Bộ nhớ 3D bền vững giữ được hình học vật thể khi bị che khuất",
            font=FONT, font_size=16, color=C_GREEN, weight=BOLD
        ).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 26 — ST4rtrack: Vấn đề truyền thống (~50s)       ║
# ╚══════════════════════════════════════════════════════════╝
class Scene26_ST4rtrackProblem(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("ST4rtrack", "Vấn đề: 2 bước riêng biệt")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Bước 1: Optical Flow ===
        step1_box = RoundedRectangle(
            width=3.8, height=1.4, corner_radius=0.12,
            color=C_RED, fill_opacity=0.1, stroke_width=2
        )
        step1_title = Text("Bước 1: Optical Flow 2D", font=FONT, font_size=15, color=C_RED, weight=BOLD)
        step1_desc = Text("Theo dõi vết điểm ảnh di chuyển", font=FONT, font_size=12, color=WHITE)
        step1_content = VGroup(step1_title, step1_desc).arrange(DOWN, buff=0.12).move_to(step1_box)
        step1_group = VGroup(step1_box, step1_content)

        # Arrow
        arrow = Arrow(
            LEFT * 1.8, RIGHT * 1.8,
            color=C_YELLOW, stroke_width=2.5
        )
        arrow_label = Text("Sai lệch ε", font=FONT, font_size=12, color=C_YELLOW)

        # Bước 2: SfM
        step2_box = RoundedRectangle(
            width=3.8, height=1.4, corner_radius=0.12,
            color=C_RED, fill_opacity=0.1, stroke_width=2
        )
        step2_title = Text("Bước 2: Structure from Motion 3D", font=FONT, font_size=15, color=C_RED, weight=BOLD)
        step2_desc = Text("Dựng mô hình 3D từ điểm 2D", font=FONT, font_size=12, color=WHITE)
        step2_content = VGroup(step2_title, step2_desc).arrange(DOWN, buff=0.12).move_to(step2_box)
        step2_group = VGroup(step2_box, step2_content)

        # Arrange pipeline (xếp hộp và mũi tên, sau đó đặt nhãn lên trên mũi tên rồi shift cả cụm)
        pipeline_no_label = VGroup(step1_group, arrow, step2_group).arrange(RIGHT, buff=0.3)
        arrow_label.next_to(arrow, UP, buff=0.15)
        pipeline = VGroup(pipeline_no_label, arrow_label).shift(UP * 0.8)

        self.play(
            FadeIn(step1_group, shift=LEFT * 0.2),
            run_time=0.6
        )
        self.wait(0.3)

        self.play(
            Create(arrow),
            FadeIn(arrow_label),
            run_time=0.5
        )
        self.wait(0.3)

        self.play(
            FadeIn(step2_group, shift=RIGHT * 0.2),
            run_time=0.6
        )
        self.wait(1)

        # === Vấn đề: Error Amplification ===
        problem_box = RoundedRectangle(
            width=9.0, height=1.2, corner_radius=0.12,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        ).shift(DOWN * 1.5)

        problem_text = VGroup(
            Text("❌ Sai số nhỏ ε từ Optical Flow → Phóng to thành 10ε ở SfM", font=FONT, font_size=14, color=C_RED, weight=BOLD),
            Text("→ Tọa độ 3D bị méo mó, mô hình sụp đổ", font=FONT, font_size=13, color=WHITE),
        ).arrange(DOWN, buff=0.12).move_to(problem_box)

        self.play(FadeIn(problem_box), FadeIn(problem_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 27 — ST4rtrack: Giải pháp (~50s)                ║
# ╚══════════════════════════════════════════════════════════╝
class Scene27_ST4rtrackSolution(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("ST4rtrack: Giải pháp")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Vấn đề cũ ===
        old_box = RoundedRectangle(
            width=4.5, height=2.0, corner_radius=0.12,
            color=C_RED, fill_opacity=0.1, stroke_width=2
        )
        old_title = Text("Phương pháp cũ", font=FONT, font_size=15, color=C_RED, weight=BOLD)
        old_steps = VGroup(
            Text("1. Optical Flow 2D", font=FONT, font_size=12, color=WHITE),
            Text("2. SfM 3D", font=FONT, font_size=12, color=WHITE),
            Text("❌ 2 bước độc lập", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        old_content = VGroup(old_title, old_steps).arrange(DOWN, buff=0.15).move_to(old_box)
        old_group = VGroup(old_box, old_content)

        # === Giải pháp mới ===
        new_box = RoundedRectangle(
            width=4.5, height=2.0, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.1, stroke_width=2
        )
        new_title = Text("ST4rtrack", font=FONT, font_size=15, color=C_GREEN, weight=BOLD)
        new_steps = VGroup(
            Text("Xử lý đồng thời", font=FONT, font_size=12, color=WHITE),
            Text("Tracking + Reconstruction", font=FONT, font_size=12, color=WHITE),
            Text("✓ 1 mô hình feed-forward", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        new_content = VGroup(new_title, new_steps).arrange(DOWN, buff=0.15).move_to(new_box)
        new_group = VGroup(new_box, new_content)

        # Arrange
        comparison = VGroup(old_group, new_group).arrange(RIGHT, buff=1.0).shift(UP * 0.5)

        # VS divider (căn giữa theo cụm so sánh để khớp chiều cao y)
        vs_text = Text("vs", font=FONT, font_size=28, color=C_YELLOW, weight=BOLD)
        vs_text.move_to(comparison.get_center())

        self.play(
            FadeIn(old_group, shift=LEFT * 0.3),
            FadeIn(vs_text),
            FadeIn(new_group, shift=RIGHT * 0.3),
            run_time=1.2
        )
        self.wait(1)

        # === Benefit ===
        benefit_box = RoundedRectangle(
            width=9.0, height=0.9, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        ).to_edge(DOWN, buff=0.8)

        benefit_text = Text(
            "✓ Hình học 3D bổ trợ ngược lại cho tracking 2D → Triệt tiêu sai số tích lũy",
            font=FONT, font_size=14, color=C_GREEN, weight=BOLD
        ).move_to(benefit_box)

        self.play(FadeIn(benefit_box), FadeIn(benefit_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 28 — ST4rtrack: Công thức (~50s)                ║
# ╚══════════════════════════════════════════════════════════╝
class Scene28_ST4rtrackFormula(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("ST4rtrack: Spatiotemporal Pointmap")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === Công thức chính ===
        formula_eq = MathTex(
            r"P_i(t) = [X_i(t), Y_i(t), Z_i(t)] \in \mathbb{R}^3",
            font_size=48, color=WHITE
        ).shift(UP * 1.2)

        self.play(Write(formula_eq), run_time=1.2)
        self.wait(1)

        # === Giải thích ===
        explain_box = RoundedRectangle(
            width=9.2, height=2.0, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        ).shift(DOWN * 0.5)

        explain_lines = VGroup(
            Text("• P_i(t): Tọa độ 3D của điểm i tại thời gian t", font=FONT, font_size=13, color=WHITE),
            Text("• X_i(t), Y_i(t), Z_i(t): Tọa độ trong không gian 3 chiều", font=FONT, font_size=13, color=WHITE),
            Text("• Mỗi điểm bề mặt được theo dõi liên tục theo thời gian", font=FONT, font_size=13, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)

        explain_lines.move_to(explain_box).shift(LEFT * 0.3)

        self.play(FadeIn(explain_box), run_time=0.5)
        for line in explain_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)

        # === Visualization: Quỹ đạo 3D ===
        trajectory_box = RoundedRectangle(
            width=7.0, height=0.8, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.5)

        trajectory_text = Text(
            "Kết quả: Quỹ đạo 3D mượt mà của nhiều điểm trên bề mặt vật thể",
            font=FONT, font_size=14, color=C_GREEN, weight=BOLD
        ).move_to(trajectory_box)

        self.play(FadeIn(trajectory_box), FadeIn(trajectory_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 29 — So sánh CUT3R vs ST4rtrack (~50s)           ║
# ╚══════════════════════════════════════════════════════════╝
class Scene29_ComparisonCUT3RST4rtrack(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("So sánh: CUT3R vs ST4rtrack")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === CUT3R ===
        cut3r_box = RoundedRectangle(
            width=4.2, height=2.6, corner_radius=0.12,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        )
        cut3r_title = Text("CUT3R", font=FONT, font_size=18, color=C_BLUE, weight=BOLD)
        cut3r_items = VGroup(
            Text("• Bộ nhớ 3D liên tục", font=FONT, font_size=12, color=WHITE),
            Text("• Recurrent Transformer", font=FONT, font_size=12, color=WHITE),
            Text("• Cập nhật real-time", font=FONT, font_size=12, color=WHITE),
            Text("• Xử lý che khuất", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        cut3r_content = VGroup(cut3r_title, cut3r_items).arrange(DOWN, buff=0.18).move_to(cut3r_box)
        cut3r_group = VGroup(cut3r_box, cut3r_content)
        cut3r_group.shift(LEFT * 4.0)

        # === ST4rtrack ===
        st4r_box = RoundedRectangle(
            width=4.2, height=2.6, corner_radius=0.12,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        )
        st4r_title = Text("ST4rtrack", font=FONT, font_size=18, color=C_GREEN, weight=BOLD)
        st4r_items = VGroup(
            Text("• Pointmap 4D", font=FONT, font_size=12, color=WHITE),
            Text("• Feed-forward model", font=FONT, font_size=12, color=WHITE),
            Text("• Tracking + Reconstruction", font=FONT, font_size=12, color=WHITE),
            Text("• Vật thể tĩnh + động", font=FONT, font_size=12, color=WHITE),
        ).arrange(DOWN, buff=0.12)
        
        st4r_content = VGroup(st4r_title, st4r_items).arrange(DOWN, buff=0.18).move_to(st4r_box)
        st4r_group = VGroup(st4r_box, st4r_content)
        st4r_group.shift(RIGHT * 4.0)

        # Common goal
        common_box = RoundedRectangle(
            width=8.5, height=1.0, corner_radius=0.12,
            color=C_PURPLE, fill_opacity=0.08, stroke_width=2
        ).to_edge(DOWN, buff=0.8)

        common_text = Text(
            "Cùng mục đích: Xây dựng structured 3D representation bền vững của thế giới",
            font=FONT, font_size=14, color=C_PURPLE, weight=BOLD
        ).move_to(common_box)

        self.play(
            FadeIn(cut3r_group, shift=LEFT * 0.3),
            FadeIn(st4r_group, shift=RIGHT * 0.3),
            run_time=1.2
        )
        self.wait(1)

        self.play(FadeIn(common_box), FadeIn(common_text), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 30 — Recap Phần 2 + Chuyển tiếp (~50s)           ║
# ╚══════════════════════════════════════════════════════════╝
class Scene30_Part2Recap(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Tổng kết phần 2")
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # === 3 keyword recap ===
        keywords = [
            ("Streaming\nPerception", "Nền tảng lý thuyết", C_BLUE),
            ("CUT3R", "Bộ nhớ 3D recurrent", C_GREEN),
            ("ST4rtrack", "Pointmap 4D", C_YELLOW),
        ]

        kw_cards = VGroup()
        for kw_name, kw_desc, col in keywords:
            box = RoundedRectangle(
                width=2.8, height=2.4, corner_radius=0.12,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            
            kw_lines = kw_name.split("\n")
            kw = VGroup(*[
                Text(line, font=FONT, font_size=16, color=WHITE) for line in kw_lines
            ]).arrange(DOWN, buff=0.08).move_to(box.get_top() + DOWN * 0.5)
            
            desc = Text(kw_desc, font=FONT, font_size=12, color=col, weight=BOLD)
            desc.move_to(box.get_center() + DOWN * 0.3)
            
            check = Text("✓", font_size=28, color=col).move_to(box.get_bottom() + UP * 0.3)
            kw_cards.add(VGroup(box, kw, desc, check))

        kw_cards.arrange(RIGHT, buff=0.4).shift(UP * 0.5)

        for card in kw_cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
            self.wait(0.3)

        # === Kết luận ===
        conclusion = Text(
            "→ Từ Pixel-only sang Structured 3D Representation: Bước tiến quan trọng",
            font=FONT, font_size=16, color=C_GREEN, weight=BOLD
        ).shift(DOWN * 1.2)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.8)
        self.wait(1)

        # === Transition ===
        transition_box = RoundedRectangle(
            width=9.0, height=1.2, corner_radius=0.12,
            color=C_RED, fill_opacity=0.08, stroke_width=2
        ).to_edge(DOWN, buff=0.5)

        transition_q = Text(
            "❓ Câu hỏi cuối cùng: Làm sao xây dựng mô hình thế giới giúp robot hành động thông minh?",
            font=FONT, font_size=14, color=WHITE
        ).move_to(transition_box)

        self.play(FadeIn(transition_box), FadeIn(transition_q), run_time=0.8)
        self.wait(2)

        # === Transition effect ===
        self.play(
            *[FadeOut(card, shift=LEFT * 2) for card in kw_cards],
            FadeOut(title, shift=UP),
            run_time=0.8
        )

        next_part = Text(
            "Phần 3: Mô hình Thế giới cho Robot",
            font=FONT, font_size=32, color=WHITE
        ).move_to(ORIGIN)
        
        self.play(FadeOut(conclusion), FadeOut(transition_box), FadeOut(transition_q))
        self.play(FadeIn(next_part), run_time=1)
        self.wait(2)
        self.play(FadeOut(next_part))


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 31 — Outro Phần 2                                ║
# ╚══════════════════════════════════════════════════════════╝
class Scene31_Part2Outro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # === Recap hành trình ===
        journey = VGroup(
            Text("Phần 1: Tạo Video AI", font=FONT, font_size=24, color=C_BLUE),
            Text("↓", font_size=28, color=C_SUB),
            Text("Phần 2: Hiểu cấu trúc 3D", font=FONT, font_size=24, color=C_GREEN),
            Text("↓", font_size=28, color=C_SUB),
            Text("Phần 3: Mô hình Thế giới", font=FONT, font_size=24, color=C_YELLOW),
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.5)

        self.play(Write(journey[0]), run_time=0.6)
        self.wait(0.3)
        self.play(Write(journey[1]), run_time=0.3)
        self.wait(0.2)
        self.play(Write(journey[2]), run_time=0.6)
        self.wait(0.3)
        self.play(Write(journey[3]), run_time=0.3)
        self.wait(0.2)
        self.play(Write(journey[4]), run_time=0.6)
        self.wait(2)

        # === Question box ===
        question_box = RoundedRectangle(
            width=9.0, height=1.5, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.5)

        question = Text(
            "Khám phá tiếp: World Models & Robotics",
            font=FONT, font_size=20, color=C_PURPLE, weight=BOLD
        ).move_to(question_box)

        self.play(FadeIn(question_box), FadeIn(question), run_time=1)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])
