# Đồ án AI: Từ Tạo Video đến Mô hình Thế giới (World Model)

Dự án sử dụng thư viện **Manim** để tạo video cung cấp kiến thức trực quan sinh động về hành trình từ Video AI đến mô hình thế giới và ứng dụng trong Robotics. Video dài khoảng 19 phút, hỗ trợ giọng nói lồng tiếng tiếng Việt tự động tạo bằng công nghệ TTS của Microsoft.

---

## 🏛️ Thông tin môn học & Giảng viên
* **Môn học:** Cơ sở Trí tuệ Nhân tạo (Khóa 2023)
* **Lớp:** 23_3
* **Giảng viên lý thuyết (GVLT):** Thầy Bùi Duy Đăng
* **Trợ giảng (TG):** Thầy Nguyễn Ngọc Đức, Cô Nguyễn Thị Thu Hằng, Thầy Nguyễn Thanh Tình
* **Giảng viên thực hành (GVTH):** Thầy Huỳnh Lâm Hải Đăng
* **Mã nguồn dự án:** [Group07_Ai_Project](https://github.com/Truc54/Group07_Ai_Project)

---


## 📚 Thông tin các bài báo được chọn nghiên cứu

1. **CUT3R: Continuous 3D Perception Model with Persistent State**
   * **Link toàn văn:** https://arxiv.org/abs/2501.12387
   * **Hội nghị:** CVPR 2025 | **Năm xuất bản:** 2025

2. **ST4rtrack: Simultaneous 4D Reconstruction and Tracking in the World**
   * **Link toàn văn:** https://arxiv.org/abs/2504.13152
   * **Hội nghị:** ICCV 2025 | **Năm xuất bản:** 2025

3. **Video as the New Language for Real-World Decision Making**
   * **Link toàn văn:** https://arxiv.org/abs/2402.17139
   * **Hội nghị:** ICML 2024 | **Năm xuất bản:** 2024

---

## 📁 Cấu trúc thư mục dự án

```text
CSAI/
│
├── 📁 scenes/                          # Mã nguồn Manim làm video
│   ├── config.py                       # CẤU HÌNH CHUNG — màu, font, helper (DÙNG CHUNG)
│   ├── part0_intro.py                  # Mở đầu (Scene 01 - 03)
│   ├── part1_video_generation.py       # Phần 1: Kiến trúc tạo video AI (Scene 04 - 17)
│   ├── part2_3d_perception.py          # Phần 2: Nhận thức 3D từ video (Scene 18 - 30)
│   ├── part3_world_models.py           # Phần 3: Mô hình thế giới cho robot (Scene 32 - 44)
│   └── part4_credits.py                # Phần kết & Credits (Scene 45 - 46)
│
├── 📁 scripts/                         # Các script tự động hóa xử lý
│   ├── generate_voiceover.py           # Tạo giọng nói AI tiếng Việt cho kịch bản
│   ├── check_duration.py              # Đo thời lượng file audio
│   ├── merge_audio_video.py            # Ghép file audio vào video tương ứng
│   └── concat_final.py                # Nối tất cả các phần thành video hoàn chỉnh
│
├── 📁 voiceover/                       # Chứa file audio tiếng Việt (được sinh tự động)
├── 📁 output/merged/                   # Chứa video sau khi ghép audio thành công
├── 📁 assets/                          # Chứa hình ảnh, tài nguyên tĩnh (nếu cần)
├── requirements.txt                    # Thư viện Python cần thiết
└── README.md                           # Tài liệu hướng dẫn này
```

---

## 🛠️ Hướng dẫn cài đặt môi trường

### 1. Cài đặt FFmpeg & LaTeX (Cần thiết cho Manim)
Trên Windows, chạy Powershell với quyền Administrator và cài qua winget:
```powershell
# Cài FFmpeg
winget install Gyan.FFmpeg
ffmpeg -version   # Kiểm tra xem cài thành công chưa
```
Tải và cài đặt **MiKTeX** để hỗ trợ hiển thị các công thức toán học đẹp mắt:
👉 Tải từ [MiKTeX Download](https://miktex.org/download)

### 2. Thiết lập Python Virtual Environment & Cài thư viện
```powershell
# Di chuyển vào thư mục dự án
cd c:\Users\truct\source\CSAI

# Tạo venv
python -m venv .venv

# Kích hoạt venv
.\.venv\Scripts\Activate.ps1

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

---

## 🚀 Hướng dẫn thực hiện dự án

### Bước 1: Sinh giọng nói AI
Chạy script sinh giọng nói từ kịch bản có sẵn:
```powershell
python scripts/generate_voiceover.py
```
Sau đó chạy kiểm tra thời lượng các file audio để điều chỉnh thời gian `wait` trong Manim:
```powershell
python scripts/check_duration.py
```

### Bước 2: Thiết kế & Render các Scene Manim
Để render chất lượng thấp để kiểm tra (480p, 15fps):
```powershell
manim -pql scenes/part1_video_generation.py Scene05_2DVAE_Problem
```
Để render chất lượng cao xuất bản (1080p, 60fps):
```powershell
manim -qh scenes/part1_video_generation.py Scene05_2DVAE_Problem
```
Render toàn bộ các scene trong một file:
```powershell
manim -qh scenes/part1_video_generation.py -a
```

### Bước 3: Ghép âm thanh & Nối video
```powershell
# 1. Ghép tiếng khớp từng scene
python scripts/merge_audio_video.py

# 2. Ghép nối tất cả các scene thành video hoàn chỉnh
python scripts/concat_final.py
```
Video cuối cùng sẽ nằm tại `output/merged/FINAL_VIDEO.mp4`.

---

## 🌿 Quy tắc làm việc nhóm & Git Workflow

### 1. Đặt tên nhánh (Branch Naming)
Tuyệt đối không push code trực tiếp lên nhánh `main`. Mọi tính năng mới hoặc sửa lỗi phải được làm ở nhánh phụ theo cú pháp:
* **Nhánh phát triển tính năng:** `feature/<tên-thành-viên>/<tác-vụ-viết-thường-khong-dau>`
* **Nhánh sửa lỗi:** `bugfix/<tên-thành-viên>/<tên-loi>`

*Ví dụ:*
- `feature/truc/config-and-scripts`
- `feature/tuan/part2-3d-perception`
- `bugfix/tuan/fix-scene05-alignment`

### 2. Quy trình gửi Pull Request (PR) đàng hoàng
Tất cả các thay đổi khi muốn gộp vào nhánh chính `main` phải thông qua Pull Request trên GitHub và được người còn lại xem qua hoặc tự rà soát cẩn thận.
* Tiêu đề PR rõ ràng, phản ánh đúng nội dung.
* Sử dụng mẫu mô tả PR dưới đây:
  ```markdown
  ### 📝 Tóm tắt thay đổi
  - Viết code Manim cho các scene từ Sc... đến Sc...
  - Đã cập nhật lời thoại và render thử không lỗi.
  
  ### 🎥 Kết quả chạy thử (Đã test local)
  - Đã render thành công chất lượng thấp (`manim -pql ...`) không có lỗi biên dịch.
  
  ### 🔍 Checklist tự kiểm tra
  - [ ] Không chỉnh sửa file `scenes/config.py` (trừ khi có sự thảo luận thống nhất).
  - [ ] Sử dụng đúng hệ màu và font chữ quy định trong `config.py`.
  - [ ] Lời thoại chính xác, không dùng từ ngữ thừa hay sai chính tả.
  - [ ] Các file output render (`.mp4`, `.png`) đã được bỏ qua và không bị commit lên Git.
  ```
