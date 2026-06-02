# scenes/part1_video_generation.py — Trực: Phần 1: Kiến trúc tạo video AI (Sc04-17)
# Render toàn bộ: manim -pql scenes/part1_video_generation.py -a
# Render 1 scene: manim -pql scenes/part1_video_generation.py Scene04_Part1Intro
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scenes.config import *


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 04 — Giới thiệu Phần 1                          ║
# ╚══════════════════════════════════════════════════════════╝
class Scene04_Part1Intro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Tiêu đề phần
        part_num = Text("PHẦN 1", font=FONT, font_size=56, color=WHITE)
        line1 = Text("Kiến trúc tạo Video AI", font=FONT, font_size=38, color=WHITE)
        line2 = Text("thế hệ mới", font=FONT, font_size=38, color=WHITE)
        part_title = VGroup(line1, line2).arrange(DOWN, buff=0.2)
        part_group = VGroup(part_num, part_title).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(part_num, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(part_title), run_time=1.2)
        self.wait(1)

        # Timeline tiến bộ
        self.play(FadeOut(part_group))
        timeline_title = Text("Tiến bộ qua các năm", font=FONT, font_size=30, color=WHITE)
        timeline_title.to_edge(UP, buff=0.6)
        self.play(FadeIn(timeline_title))

        line = Line(LEFT * 5, RIGHT * 5, color=C_SUB, stroke_width=2).shift(DOWN * 0.3)
        self.play(Create(line))

        years = ["2022", "2023", "2024", "2025"]
        descs = ["Video ngắn\nnhòe mờ", "Video 10s\n512px", "Video 30s\n720p", "Video 2 phút\n1080p · 30fps"]
        colors = [C_RED, C_YELLOW, C_BLUE, C_GREEN]

        for i, (year, desc, col) in enumerate(zip(years, descs, colors)):
            x_pos = LEFT * 3.75 + RIGHT * 2.5 * i
            dot = Dot(point=x_pos + DOWN * 0.3, radius=0.12, color=col)
            y_label = Text(year, font=FONT, font_size=22, color=WHITE).next_to(dot, DOWN, buff=0.25)
            d_label = Text(desc, font=FONT, font_size=16, color=WHITE, line_spacing=1.1).next_to(y_label, DOWN, buff=0.2)
            self.play(FadeIn(dot, scale=0.5), FadeIn(y_label), run_time=0.5)
            self.play(FadeIn(d_label, shift=UP * 0.2), run_time=0.4)

        question = Text(
            "Đằng sau sự tiến bộ này là\nnhững đột phá kỹ thuật nào?",
            font=FONT, font_size=28, color=WHITE, line_spacing=1.2
        ).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(question), run_time=1)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 05 — Vấn đề: 2D VAE xử lý khung hình đơn lẻ    ║
# ╚══════════════════════════════════════════════════════════╝
class Scene05_2DVAE_Problem(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vấn đề: 2D VAE truyền thống")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 5 khung hình riêng lẻ
        frames = VGroup()
        for i in range(5):
            rect = RoundedRectangle(
                width=1.6, height=1.2, corner_radius=0.1,
                color=C_BLUE, fill_opacity=0.15, stroke_width=2
            )
            label = Text(f"F{i+1}", font=FONT, font_size=18, color=WHITE).move_to(rect)
            frames.add(VGroup(rect, label))
        frames.arrange(RIGHT, buff=0.25).shift(UP * 0.5)

        self.play(LaggedStart(*[FadeIn(f, scale=0.8) for f in frames], lag_ratio=0.15))
        self.wait(0.5)

        # Mũi tên encoder riêng biệt
        arrows_down = VGroup()
        encoders = VGroup()
        for f in frames:
            arrow = Arrow(
                f.get_bottom(), f.get_bottom() + DOWN * 0.9,
                color=C_RED, stroke_width=2, buff=0.1, max_tip_length_to_length_ratio=0.2
            )
            enc = Text("Enc", font=FONT, font_size=14, color=WHITE).next_to(arrow, RIGHT, buff=0.05)
            arrows_down.add(arrow)
            encoders.add(enc)

        self.play(
            LaggedStart(*[Create(a) for a in arrows_down], lag_ratio=0.1),
            LaggedStart(*[FadeIn(e) for e in encoders], lag_ratio=0.1),
        )
        self.wait(0.5)

        # Output frames riêng lẻ
        out_frames = VGroup()
        for i, f in enumerate(frames):
            rect = RoundedRectangle(
                width=1.6, height=1.2, corner_radius=0.1,
                color=C_RED, fill_opacity=0.1, stroke_width=2, stroke_color=C_RED
            )
            label = Text(f"F'{i+1}", font=FONT, font_size=18, color=WHITE).move_to(rect)
            g = VGroup(rect, label)
            g.move_to(f.get_bottom() + DOWN * 1.8)
            out_frames.add(g)

        self.play(LaggedStart(*[FadeIn(o, shift=DOWN * 0.3) for o in out_frames], lag_ratio=0.1))

        # Dấu cách ly
        isolation = VGroup()
        for i in range(4):
            cross = make_cross(size=0.25, stroke_width=3, color=C_RED)
            cross.move_to((frames[i].get_right() + frames[i + 1].get_left()) / 2)
            isolation.add(cross)
        self.play(LaggedStart(*[FadeIn(s, scale=2) for s in isolation], lag_ratio=0.1))

        error_text = Text(
            "→ Mỗi frame xử lý ĐỘC LẬP, không biết frame trước/sau!",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(error_text))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 06 — Hậu quả: Flickering, biến dạng             ║
# ╚══════════════════════════════════════════════════════════╝
class Scene06_Flickering(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Hậu quả của 2D VAE")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 3 lỗi minh họa
        errors = [
            ("1. Flickering", "Ánh sáng & màu sắc\nthay đổi đột ngột", C_YELLOW),
            ("2. Biến dạng cấu trúc", "Vật thể bị méo\nkhi chuyển động", C_RED),
            ("3. Temporal Inconsistency", "Vật thể biến mất\nrồi xuất hiện lại", C_PURPLE),
        ]

        cards = VGroup()
        for err_title, err_desc, col in errors:
            box = RoundedRectangle(
                width=3.5, height=2.8, corner_radius=0.15,
                color=col, fill_opacity=0.08, stroke_width=2
            )
            t = Text(err_title, font=FONT, font_size=20, color=WHITE).move_to(box.get_top() + DOWN * 0.5)
            d = Text(err_desc, font=FONT, font_size=16, color=WHITE, line_spacing=1.2).next_to(t, DOWN, buff=0.3)
            cross = make_cross(size=0.4, stroke_width=4, color=C_RED).move_to(box.get_bottom() + UP * 0.5)
            cards.add(VGroup(box, t, d, cross))

        cards.arrange(RIGHT, buff=0.4).shift(DOWN * 0.3)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.7)
            self.wait(0.8)

        conclusion = Text(
            "→ 2D VAE không đủ cho video chất lượng cao!",
            font=FONT, font_size=24, color=WHITE
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(conclusion))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 07 — Giải pháp: 3D VAE — Ý tưởng                ║
# ╚══════════════════════════════════════════════════════════╝
class Scene07_3DVAE_Idea(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Giải pháp: 3D VAE", "Nén toàn bộ video cùng lúc")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # === BÊN TRÁI: 2D VAE (rời rạc) ===
        left_label = Text("2D VAE", font=FONT, font_size=24, color=WHITE)
        left_frames = VGroup()
        for i in range(4):
            r = Square(side_length=0.8, color=C_RED, fill_opacity=0.15, stroke_width=1.5)
            t = Text(f"F{i+1}", font=FONT, font_size=14, color=WHITE).move_to(r)
            left_frames.add(VGroup(r, t))
        left_frames.arrange(RIGHT, buff=0.15)
        left_group = VGroup(left_label, left_frames).arrange(DOWN, buff=0.3)
        left_group.move_to(LEFT * 3.2 + DOWN * 0.5)

        # Dấu X ở giữa các frame
        left_crosses = VGroup()
        for i in range(3):
            x = make_cross(size=0.18, stroke_width=2, color=C_RED)
            x.move_to((left_frames[i].get_right() + left_frames[i + 1].get_left()) / 2)
            left_crosses.add(x)

        # === BÊN PHẢI: 3D VAE (liên tục) ===
        right_label = Text("3D VAE", font=FONT, font_size=24, color=WHITE)
        cube = Prism(
            dimensions=[2.5, 1.0, 0.8],
            fill_opacity=0.15, fill_color=C_GREEN,
            stroke_width=1.5, stroke_color=C_GREEN
        )
        cube_label_h = Text("H", font=FONT, font_size=14, color=WHITE)
        cube_label_w = Text("W", font=FONT, font_size=14, color=WHITE)
        cube_label_t = Text("T", font=FONT, font_size=14, color=WHITE)

        right_group = VGroup(right_label, cube).arrange(DOWN, buff=0.3)
        right_group.move_to(RIGHT * 2 + DOWN * 0.5)

        cube_label_t.next_to(cube, RIGHT, buff=0.15)
        cube_label_h.next_to(cube, UP, buff=0.1)
        cube_label_w.next_to(cube, DOWN, buff=0.1)

        # VS divider
        vs_text = Text("vs", font=FONT, font_size=28, color=C_SUB).move_to(DOWN * 0.5)

        # Animate
        self.play(FadeIn(left_label, shift=DOWN * 0.2))
        self.play(LaggedStart(*[FadeIn(f) for f in left_frames], lag_ratio=0.1))
        self.play(LaggedStart(*[FadeIn(x, scale=2) for x in left_crosses], lag_ratio=0.1))
        self.wait(0.5)

        self.play(FadeIn(vs_text))
        self.play(FadeIn(right_label, shift=DOWN * 0.2))
        self.play(FadeIn(cube, shift=LEFT * 0.3), run_time=0.8)
        self.play(FadeIn(cube_label_t), FadeIn(cube_label_h), FadeIn(cube_label_w))

        # Arrow compression
        compress_arrow = Arrow(
            cube.get_right() + RIGHT * 0.2, cube.get_right() + RIGHT * 1.2,
            color=C_YELLOW, stroke_width=3
        )
        small_cube = Prism(
            dimensions=[0.8, 0.4, 0.3],
            fill_opacity=0.3, fill_color=C_YELLOW,
            stroke_width=1.5, stroke_color=C_YELLOW
        ).next_to(compress_arrow, RIGHT, buff=0.15)
        z_label = Text("z (latent)", font=FONT, font_size=14, color=WHITE).next_to(small_cube, DOWN, buff=0.15)

        self.play(Create(compress_arrow), FadeIn(small_cube, shift=LEFT * 0.2), FadeIn(z_label))

        conclusion = Text(
            "✓ Nén đồng thời 3 chiều → giữ liên tục giữa các frame",
            font=FONT, font_size=22, color=WHITE
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(conclusion))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 08 — 3D VAE: Công thức toán học                  ║
# ╚══════════════════════════════════════════════════════════╝
class Scene08_3DVAE_Math(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("3D VAE: Biểu diễn toán học")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Input tensor
        input_label = Text("Video đầu vào:", font=FONT, font_size=22, color=WHITE)
        input_eq = MathTex(
            r"V \in \mathbb{R}^{T \times C \times H \times W}",
            font_size=40, color=WHITE
        )
        input_eq.next_to(input_label, RIGHT, buff=0.3).shift(UP * 0.08)
        input_group = VGroup(input_label, input_eq).move_to(UP * 1.8)

        self.play(FadeIn(input_group))
        self.wait(1)

        # Encoder arrow
        enc_arrow = Arrow(ORIGIN + UP * 0.5, ORIGIN + DOWN * 0.5, color=C_YELLOW, stroke_width=3)
        enc_arrow.move_to(UP * 0.7)
        enc_text = Text("Encoder 3D", font=FONT, font_size=20, color=WHITE).next_to(enc_arrow, RIGHT, buff=0.2)
        self.play(Create(enc_arrow), FadeIn(enc_text))

        # Latent
        lat_label = Text("Latent space:", font=FONT, font_size=22, color=WHITE)
        lat_eq = MathTex(
            r"z \in \mathbb{R}^{\hat{T} \times \hat{C} \times \hat{H} \times \hat{W}}",
            font_size=40, color=WHITE
        )
        lat_eq.next_to(lat_label, RIGHT, buff=0.3).shift(UP * 0.08)
        lat_group = VGroup(lat_label, lat_eq).move_to(DOWN * 0.2)

        self.play(FadeIn(lat_group))
        self.wait(1)

        # Highlight compression ratios
        compress_box = RoundedRectangle(
            width=8, height=1.8, corner_radius=0.15,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=1.5
        ).shift(DOWN * 2)

        t1 = Text("Nén thời gian:", font=FONT, font_size=20, color=WHITE)
        m1 = MathTex(r"\hat{T} < T", font_size=32, color=WHITE)
        t2 = Text("    Nén không gian:", font=FONT, font_size=20, color=WHITE)
        m2 = MathTex(r"\hat{H} < H, \; \hat{W} < W", font_size=32, color=WHITE)
        
        m1.next_to(t1, RIGHT, buff=0.25).shift(UP * 0.08)
        t2.next_to(m1, RIGHT, buff=0.4)
        m2.next_to(t2, RIGHT, buff=0.25).shift(UP * 0.08)
        
        comp_items = VGroup(t1, m1, t2, m2).move_to(compress_box)

        self.play(FadeIn(compress_box), FadeIn(comp_items), run_time=1)

        benefit = Text(
            "→ Chi phí tính toán giảm đáng kể, chuyển động vẫn mịn màng",
            font=FONT, font_size=20, color=WHITE
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(benefit))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 09 — 3D VAE: Minh họa nén trực quan             ║
# ╚══════════════════════════════════════════════════════════╝
class Scene09_3DVAE_Visual(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("3D VAE: Minh họa trực quan")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Video gốc: khối lớn
        original_label = Text("Video gốc", font=FONT, font_size=22, color=WHITE)
        original_label.move_to(UP * 1.5 + LEFT * 4)

        orig_box = RoundedRectangle(
            width=3, height=2, corner_radius=0.15,
            color=C_BLUE, fill_opacity=0.15, stroke_width=2
        ).next_to(original_label, DOWN, buff=0.3)

        orig_dims = VGroup(
            Text("16 frames", font=FONT, font_size=16, color=WHITE),
            Text("256 × 256 px", font=FONT, font_size=16, color=WHITE),
        ).arrange(DOWN, buff=0.15).move_to(orig_box)

        self.play(FadeIn(original_label), FadeIn(orig_box), FadeIn(orig_dims))
        self.wait(0.5)

        # Arrow
        compress_arrow = Arrow(
            orig_box.get_right() + RIGHT * 0.2, orig_box.get_right() + RIGHT * 2.5,
            color=C_YELLOW, stroke_width=3
        )
        arrow_label = VGroup(
            Text("3D VAE", font=FONT, font_size=18, color=WHITE),
            Text("Nén T×4, HW×8", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.1).next_to(compress_arrow, UP, buff=0.15)

        self.play(Create(compress_arrow), FadeIn(arrow_label))

        # Latent: khối nhỏ
        lat_box = RoundedRectangle(
            width=1.5, height=1.2, corner_radius=0.1,
            color=C_GREEN, fill_opacity=0.2, stroke_width=2
        ).next_to(compress_arrow, RIGHT, buff=0.3)

        lat_dims = VGroup(
            Text("4 tokens", font=FONT, font_size=14, color=WHITE),
            Text("32 × 32", font=FONT, font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.1).move_to(lat_box)

        self.play(FadeIn(lat_box, scale=0.5), FadeIn(lat_dims))
        self.wait(0.5)

        # Highlight giảm
        reduce_box = RoundedRectangle(
            width=5, height=1.2, corner_radius=0.15,
            color=C_RED, fill_opacity=0.1, stroke_width=2
        ).shift(DOWN * 2)

        reduce_text = VGroup(
            Text("Giảm ", font=FONT, font_size=28, color=WHITE),
            Text("256×", font=FONT, font_size=36, color=C_RED, weight=BOLD),
            Text(" dữ liệu", font=FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(reduce_box)

        sub_text = Text(
            "Thông tin chuyển động vẫn được bảo toàn!",
            font=FONT, font_size=20, color=WHITE
        ).next_to(reduce_box, DOWN, buff=0.25)

        self.play(FadeIn(reduce_box), FadeIn(reduce_text), run_time=0.8)
        self.play(FadeIn(sub_text))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 10 — Spatiotemporal Attention: Ý tưởng           ║
# ╚══════════════════════════════════════════════════════════╝
class Scene10_SpatiotemporalAttention(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Spatiotemporal Attention", "Attention xuyên không gian & thời gian")
        self.play(FadeIn(title), run_time=1)
        self.wait(0.5)

        # === BÊN TRÁI: Self-Attention thường (1 frame) ===
        left_label = Text("Self-Attention thường", font=FONT, font_size=18, color=WHITE)
        left_label.move_to(LEFT * 3.5 + UP * 1)

        # Grid 3x3 (1 frame)
        left_grid = VGroup()
        for r in range(3):
            for c in range(3):
                sq = Square(side_length=0.5, color=C_SUB, fill_opacity=0.1, stroke_width=1)
                sq.move_to(LEFT * 3.5 + RIGHT * c * 0.6 + DOWN * r * 0.6)
                left_grid.add(sq)

        left_frame_label = Text("Frame 1", font=FONT, font_size=14, color=WHITE)
        left_frame_label.next_to(left_grid, DOWN, buff=0.2)

        # Highlight center token attention -> only same frame
        center_sq = left_grid[4]  # center
        center_highlight = Square(side_length=0.5, color=C_YELLOW, fill_opacity=0.4, stroke_width=2)
        center_highlight.move_to(center_sq)

        left_arrows = VGroup()
        for i, sq in enumerate(left_grid):
            if i != 4:
                arr = Arrow(
                    center_sq.get_center(), sq.get_center(),
                    color=C_YELLOW, stroke_width=1.5, buff=0.15,
                    max_tip_length_to_length_ratio=0.3
                )
                left_arrows.add(arr)

        self.play(FadeIn(left_label), LaggedStart(*[FadeIn(s) for s in left_grid], lag_ratio=0.02))
        self.play(FadeIn(left_frame_label))
        self.play(FadeIn(center_highlight))
        self.play(LaggedStart(*[Create(a) for a in left_arrows], lag_ratio=0.05))

        left_note = Text("Chỉ trong 1 frame", font=FONT, font_size=16, color=WHITE)
        left_note.next_to(left_frame_label, DOWN, buff=0.2)
        self.play(FadeIn(left_note))
        self.wait(1)

        # === BÊN PHẢI: Spatiotemporal Attention (3 frames) ===
        right_label = Text("Spatiotemporal Attention", font=FONT, font_size=18, color=WHITE)
        right_label.move_to(RIGHT * 3.5 + UP * 1)

        right_grids = VGroup()
        frame_labels_r = VGroup()
        for f in range(3):
            grid = VGroup()
            for r in range(2):
                for c in range(2):
                    sq = Square(side_length=0.45, color=C_SUB, fill_opacity=0.1, stroke_width=1)
                    sq.move_to(RIGHT * (2.2 + f * 1.5) + RIGHT * c * 0.55 + DOWN * r * 0.55 + DOWN * 0.3)
                    grid.add(sq)
            right_grids.add(grid)
            fl = Text(f"F{f+1}", font=FONT, font_size=12, color=WHITE)
            fl.next_to(grid, DOWN, buff=0.15)
            frame_labels_r.add(fl)

        self.play(FadeIn(right_label))
        for g, fl in zip(right_grids, frame_labels_r):
            self.play(LaggedStart(*[FadeIn(s) for s in g], lag_ratio=0.02), FadeIn(fl), run_time=0.3)

        # Highlight 1 token -> attention to ALL tokens in ALL frames
        target = right_grids[0][0]
        t_highlight = Square(side_length=0.45, color=C_GREEN, fill_opacity=0.4, stroke_width=2)
        t_highlight.move_to(target)

        cross_arrows = VGroup()
        for grid in right_grids:
            for sq in grid:
                if sq is not target:
                    arr = Line(
                        target.get_center(), sq.get_center(),
                        color=C_GREEN, stroke_width=1, stroke_opacity=0.5
                    )
                    cross_arrows.add(arr)

        self.play(FadeIn(t_highlight))
        self.play(LaggedStart(*[Create(a) for a in cross_arrows], lag_ratio=0.02), run_time=1)

        right_note = Text("Xuyên tất cả frames!", font=FONT, font_size=16, color=WHITE)
        right_note.next_to(frame_labels_r, DOWN, buff=0.3)
        self.play(FadeIn(right_note))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 11 — Spatiotemporal Attention: Ứng dụng          ║
# ╚══════════════════════════════════════════════════════════╝
class Scene11_STA_Applications(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Spatiotemporal Attention: Ứng dụng")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 3 ứng dụng
        apps = [
            ("Vật thể di chuyển nhanh", "Không bị nhòe\nhay biến mất", "✓", C_GREEN),
            ("Camera xoay/chuyển cảnh", "Không bị rách hình\nkhi thay đổi góc", "✓", C_GREEN),
            ("Cấu trúc phức tạp", "Giữ nguyên chi tiết\n(ngón tay, lông chim...)", "✓", C_GREEN),
        ]

        cards = VGroup()
        for app_title, app_desc, check, col in apps:
            box = RoundedRectangle(
                width=3.5, height=2.8, corner_radius=0.15,
                color=col, fill_opacity=0.06, stroke_width=1.5
            )
            t = Text(app_title, font=FONT, font_size=18, color=WHITE).move_to(box.get_top() + DOWN * 0.5)
            d = Text(app_desc, font=FONT, font_size=15, color=WHITE, line_spacing=1.2).next_to(t, DOWN, buff=0.35)
            c = Text(check, font_size=40, color=C_GREEN).move_to(box.get_bottom() + UP * 0.45)
            cards.add(VGroup(box, t, d, c))

        cards.arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.6)
            self.wait(0.6)

        conclusion = Text(
            "Spatiotemporal Attention = xử lý chuyển động phức tạp hoàn hảo",
            font=FONT, font_size=20, color=WHITE
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(conclusion))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 12 — Diffusion Transformer (DiT)                 ║
# ╚══════════════════════════════════════════════════════════╝
class Scene12_DiT(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Diffusion Transformer (DiT)")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Pipeline: Noise -> DiT steps -> Clean video
        steps_count = 5
        step_boxes = VGroup()

        # Noise box
        noise_box = RoundedRectangle(
            width=1.8, height=1.3, corner_radius=0.1,
            color=C_RED, fill_opacity=0.15, stroke_width=2
        )
        noise_label = Text("Random\nNoise", font=FONT, font_size=14, color=WHITE, line_spacing=1.1).move_to(noise_box)
        noise = VGroup(noise_box, noise_label)

        # DiT step boxes
        dit_steps = VGroup()
        for i in range(steps_count):
            opacity = 0.15 + (i * 0.15)
            col_lerp = interpolate_color(ManimColor(C_RED), ManimColor(C_GREEN), i / (steps_count - 1))
            box = RoundedRectangle(
                width=1.2, height=1.0, corner_radius=0.08,
                color=col_lerp, fill_opacity=opacity, stroke_width=1.5
            )
            step_label = Text(f"Step {i+1}", font=FONT, font_size=12, color=WHITE).move_to(box)
            dit_steps.add(VGroup(box, step_label))

        # Clean video box
        clean_box = RoundedRectangle(
            width=1.8, height=1.3, corner_radius=0.1,
            color=C_GREEN, fill_opacity=0.25, stroke_width=2
        )
        clean_label = Text("Video\nSạch", font=FONT, font_size=14, color=WHITE, line_spacing=1.1).move_to(clean_box)
        clean = VGroup(clean_box, clean_label)

        # Arrange
        full_pipeline = VGroup(noise, *dit_steps, clean).arrange(RIGHT, buff=0.25)
        full_pipeline.shift(DOWN * 0.2)

        # Animate noise
        self.play(FadeIn(noise, scale=0.8))
        self.wait(0.3)

        # Animate arrows + dit steps
        for i, step in enumerate(dit_steps):
            prev = noise if i == 0 else dit_steps[i - 1]
            arr = Arrow(
                prev.get_right(), step.get_left(),
                color=C_YELLOW, stroke_width=2, buff=0.05,
                max_tip_length_to_length_ratio=0.4
            )
            self.play(Create(arr), FadeIn(step, shift=LEFT * 0.2), run_time=0.35)

        # Final arrow + clean video
        final_arr = Arrow(
            dit_steps[-1].get_right(), clean.get_left(),
            color=C_GREEN, stroke_width=2, buff=0.05,
            max_tip_length_to_length_ratio=0.4
        )
        self.play(Create(final_arr), FadeIn(clean, scale=0.8), run_time=0.5)

        # Description
        desc_box = RoundedRectangle(
            width=10, height=1.2, corner_radius=0.1,
            color=C_BOX, fill_opacity=0.3, stroke_width=1
        ).to_edge(DOWN, buff=0.3)

        desc = VGroup(
            Text("Diffusion", font=FONT, font_size=18, color=WHITE),
            Text(" = sinh dữ liệu từ noise  |  ", font=FONT, font_size=16, color=WHITE),
            Text("Transformer", font=FONT, font_size=18, color=WHITE),
            Text(" = mô hình hóa quan hệ token", font=FONT, font_size=16, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(desc_box)

        self.play(FadeIn(desc_box), FadeIn(desc))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 13 — Kiến trúc thống nhất: Vấn đề riêng lẻ      ║
# ╚══════════════════════════════════════════════════════════╝
class Scene13_SeparateModels(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Vấn đề: Mỗi tác vụ một mô hình riêng")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 3 mô hình riêng biệt
        models = [
            ("Tạo video\ntừ văn bản", "Model A\n(T2V)", C_BLUE),
            ("Chỉnh sửa\nvideo", "Model B\n(Editing)", C_YELLOW),
            ("Hiểu nội\ndung video", "Model C\n(Understanding)", C_PURPLE),
        ]

        model_groups = VGroup()
        for task_name, model_name, col in models:
            # Task box
            task_box = RoundedRectangle(
                width=2.8, height=1.3, corner_radius=0.12,
                color=C_SUB, fill_opacity=0.08, stroke_width=1.5
            )
            task_label = Text(task_name, font=FONT, font_size=16, color=WHITE, line_spacing=1.1).move_to(task_box)

            # Arrow down
            arr = Arrow(task_box.get_bottom(), task_box.get_bottom() + DOWN * 0.8,
                        color=col, stroke_width=2, buff=0.05)

            # Model box
            model_box = RoundedRectangle(
                width=2.8, height=1.3, corner_radius=0.12,
                color=col, fill_opacity=0.12, stroke_width=2
            ).next_to(arr, DOWN, buff=0.05)
            model_label = Text(model_name, font=FONT, font_size=16, color=WHITE, line_spacing=1.1).move_to(model_box)

            model_groups.add(VGroup(task_box, task_label, arr, model_box, model_label))

        model_groups.arrange(RIGHT, buff=0.4).shift(DOWN * 0.2)

        for mg in model_groups:
            self.play(FadeIn(mg, shift=UP * 0.3), run_time=0.6)
            self.wait(0.3)

        # Dấu X giữa các model
        crosses = VGroup()
        for i in range(2):
            x = make_cross(size=0.35, stroke_width=3, color=C_RED)
            x.move_to((model_groups[i].get_right() + model_groups[i + 1].get_left()) / 2)
            crosses.add(x)
        self.play(LaggedStart(*[FadeIn(x, scale=2) for x in crosses], lag_ratio=0.2))

        problem = Text(
            "3 mô hình riêng biệt → Lãng phí & không chia sẻ kiến thức!",
            font=FONT, font_size=20, color=WHITE
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(problem))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 14 — Kiến trúc thống nhất: MVL                   ║
# ╚══════════════════════════════════════════════════════════╝
class Scene14_UnifiedMVL(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Kiến trúc thống nhất: MVL")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Input modalities
        inputs = [
            ("📝 Text", C_BLUE),
            ("🖼️ Image", C_GREEN),
            ("🎬 Video", C_PURPLE),
        ]

        input_boxes = VGroup()
        for inp_name, col in inputs:
            box = make_box(inp_name, w=2.2, h=0.9, color=col)
            input_boxes.add(box)
        input_boxes.arrange(RIGHT, buff=0.3).move_to(UP * 1.8)

        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.2) for b in input_boxes], lag_ratio=0.15))
        self.wait(0.3)

        # Tokenizers
        tok_arrows = VGroup()
        tok_labels = VGroup()
        for ib in input_boxes:
            arr = Arrow(
                ib.get_bottom(), ib.get_bottom() + DOWN * 0.8,
                color=C_YELLOW, stroke_width=2, buff=0.1
            )
            tok = Text("Tokenizer", font=FONT, font_size=12, color=C_YELLOW).next_to(arr, RIGHT, buff=0.05)
            tok_arrows.add(arr)
            tok_labels.add(tok)

        self.play(
            LaggedStart(*[Create(a) for a in tok_arrows], lag_ratio=0.1),
            LaggedStart(*[FadeIn(t) for t in tok_labels], lag_ratio=0.1),
        )

        # Unified token sequence
        token_bar = RoundedRectangle(
            width=8, height=0.7, corner_radius=0.1,
            color=C_YELLOW, fill_opacity=0.15, stroke_width=2
        ).shift(DOWN * 0.1)
        token_label = Text(
            "Chuỗi Token thống nhất",
            font=FONT, font_size=18, color=C_YELLOW
        ).move_to(token_bar)

        self.play(FadeIn(token_bar), FadeIn(token_label))
        self.wait(0.5)

        # DiT Core
        dit_arrow = Arrow(
            token_bar.get_bottom(), token_bar.get_bottom() + DOWN * 0.8,
            color=C_GREEN, stroke_width=3, buff=0.1
        )
        dit_box = RoundedRectangle(
            width=4, height=1.2, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.15, stroke_width=2
        ).next_to(dit_arrow, DOWN, buff=0.1)
        dit_label = Text("DiT Core", font=FONT, font_size=24, color=WHITE, weight=BOLD).move_to(dit_box)

        self.play(Create(dit_arrow), FadeIn(dit_box), FadeIn(dit_label))
        self.wait(0.5)

        # Output
        out_arrow = Arrow(
            dit_box.get_bottom(), dit_box.get_bottom() + DOWN * 0.6,
            color=C_GREEN, stroke_width=3, buff=0.1
        )
        out_label = Text(
            "Video 1080p · 30fps · 2 phút",
            font=FONT, font_size=20, color=WHITE
        ).next_to(out_arrow, DOWN, buff=0.15)

        self.play(Create(out_arrow), FadeIn(out_label))

        # Kling examples
        examples = Text(
            "Kling · LivePortrait · Kling-Avatar",
            font=FONT, font_size=16, color=WHITE
        ).next_to(out_label, DOWN, buff=0.2)
        self.play(FadeIn(examples))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 15 — 4 hướng nghiên cứu (Mục 1-2)               ║
# ╚══════════════════════════════════════════════════════════╝
class Scene15_Research1_2(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("4 hướng nghiên cứu chính", "Hướng 1 & 2")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Hướng 1
        h1_box = RoundedRectangle(
            width=10, height=2.2, corner_radius=0.15,
            color=C_BLUE, fill_opacity=0.08, stroke_width=2
        ).shift(UP * 0.3)

        h1_num = Text("①", font_size=36, color=WHITE).move_to(h1_box.get_left() + RIGHT * 0.6)
        h1_title = Text(
            "Nâng cấp kiến trúc & thuật toán",
            font=FONT, font_size=22, color=WHITE
        ).next_to(h1_num, RIGHT, buff=0.3)
        h1_desc = Text(
            "Tối ưu cấu trúc DiT, đẩy nhanh tốc độ hội tụ Diffusion",
            font=FONT, font_size=16, color=WHITE
        ).next_to(h1_title, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(h1_box), FadeIn(h1_num), FadeIn(h1_title), run_time=0.8)
        self.play(FadeIn(h1_desc, shift=UP * 0.1))
        self.wait(1)

        # Hướng 2
        h2_box = RoundedRectangle(
            width=10, height=2.2, corner_radius=0.15,
            color=C_GREEN, fill_opacity=0.08, stroke_width=2
        ).shift(DOWN * 2.2)

        h2_num = Text("②", font_size=36, color=WHITE).move_to(h2_box.get_left() + RIGHT * 0.6)
        h2_title = Text(
            "Tăng cường tương tác & điều khiển",
            font=FONT, font_size=22, color=WHITE
        ).next_to(h2_num, RIGHT, buff=0.3)
        h2_desc = Text(
            "Điều khiển camera (Pan, Zoom, Tilt) + nhận biết vật lý",
            font=FONT, font_size=16, color=WHITE
        ).next_to(h2_title, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(h2_box), FadeIn(h2_num), FadeIn(h2_title), run_time=0.8)
        self.play(FadeIn(h2_desc, shift=UP * 0.1))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 16 — 4 hướng nghiên cứu (Mục 3-4)               ║
# ╚══════════════════════════════════════════════════════════╝
class Scene16_Research3_4(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("4 hướng nghiên cứu chính", "Hướng 3 & 4")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # Hướng 3
        h3_box = RoundedRectangle(
            width=10, height=2.2, corner_radius=0.15,
            color=C_YELLOW, fill_opacity=0.08, stroke_width=2
        ).shift(UP * 0.3)

        h3_num = Text("③", font_size=36, color=WHITE).move_to(h3_box.get_left() + RIGHT * 0.6)
        h3_title = Text(
            "Đánh giá & căn chỉnh chính xác",
            font=FONT, font_size=22, color=WHITE
        ).next_to(h3_num, RIGHT, buff=0.3)
        h3_desc = Text(
            "Đo lường chân thực vật lý + liên kết nội dung với prompt",
            font=FONT, font_size=16, color=WHITE
        ).next_to(h3_title, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(h3_box), FadeIn(h3_num), FadeIn(h3_title), run_time=0.8)
        self.play(FadeIn(h3_desc, shift=UP * 0.1))
        self.wait(1)

        # Hướng 4
        h4_box = RoundedRectangle(
            width=10, height=2.2, corner_radius=0.15,
            color=C_PURPLE, fill_opacity=0.08, stroke_width=2
        ).shift(DOWN * 2.2)

        h4_num = Text("④", font_size=36, color=WHITE).move_to(h4_box.get_left() + RIGHT * 0.6)
        h4_title = Text(
            "Nhận thức & suy luận đa phương thức",
            font=FONT, font_size=22, color=WHITE
        ).next_to(h4_num, RIGHT, buff=0.3)
        h4_desc = Text(
            "Mô hình không chỉ vẽ — mà còn giải thích cấu trúc chuyển động",
            font=FONT, font_size=16, color=WHITE
        ).next_to(h4_title, DOWN, buff=0.2, aligned_edge=LEFT)

        highlight = RoundedRectangle(
            width=4, height=0.5, corner_radius=0.1,
            color=C_PURPLE, fill_opacity=0.2, stroke_width=1
        ).move_to(h4_desc.get_center())

        self.play(FadeIn(h4_box), FadeIn(h4_num), FadeIn(h4_title), run_time=0.8)
        self.play(FadeIn(h4_desc, shift=UP * 0.1))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ╔══════════════════════════════════════════════════════════╗
# ║  SCENE 17 — Recap Phần 1 + Chuyển tiếp sang Phần 2      ║
# ╚══════════════════════════════════════════════════════════╝
class Scene17_Part1Recap(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = make_title("Tổng kết Phần 1")
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        # 4 keyword recap
        keywords = [
            ("3D VAE", "Nén đồng thời\nkhông-thời gian", C_BLUE),
            ("Spatiotemporal\nAttention", "Attend xuyên\ncác frame", C_GREEN),
            ("DiT", "Sinh video\ntừ noise", C_YELLOW),
            ("MVL", "1 mô hình\ncho mọi tác vụ", C_PURPLE),
        ]

        kw_cards = VGroup()
        for kw_title, kw_desc, col in keywords:
            box = RoundedRectangle(
                width=2.5, height=2.4, corner_radius=0.15,
                color=col, fill_opacity=0.1, stroke_width=2
            )
            t = Text(kw_title, font=FONT, font_size=18, color=WHITE, line_spacing=1.1).move_to(box.get_top() + DOWN * 0.55)
            d = Text(kw_desc, font=FONT, font_size=14, color=WHITE, line_spacing=1.1).move_to(box.get_center() + DOWN * 0.3)
            check = Text("✓", font_size=28, color=col).move_to(box.get_bottom() + UP * 0.35)
            kw_cards.add(VGroup(box, t, d, check))

        kw_cards.arrange(RIGHT, buff=0.25).shift(UP * 0.1)

        for card in kw_cards:
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.5)
            self.wait(0.3)

        self.wait(1)

        # Câu hỏi chuyển tiếp
        transition_box = RoundedRectangle(
            width=10, height=1.5, corner_radius=0.15,
            color=C_RED, fill_opacity=0.1, stroke_width=2
        ).to_edge(DOWN, buff=0.4)

        question = VGroup(
            Text("Video đẹp là chưa đủ!", font=FONT, font_size=22, color=WHITE),
            Text(
                "Liệu mô hình có thực sự hiểu cấu trúc 3D của thế giới?",
                font=FONT, font_size=20, color=WHITE
            ),
        ).arrange(DOWN, buff=0.15).move_to(transition_box)

        self.play(FadeIn(transition_box), FadeIn(question), run_time=1)
        self.wait(2)

        # Transition effect
        self.play(
            *[FadeOut(card, shift=LEFT * 2) for card in kw_cards],
            FadeOut(title, shift=UP),
            run_time=0.8
        )

        next_part = Text("→ Phần 2: Nhận thức 3D liên tục từ video",
                         font=FONT, font_size=28, color=WHITE)
        next_part.move_to(ORIGIN)
        self.play(FadeOut(transition_box), FadeOut(question))
        self.play(FadeIn(next_part), run_time=1)
        self.wait(2)
        self.play(FadeOut(next_part))
