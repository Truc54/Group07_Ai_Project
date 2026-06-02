import os
import sys
import subprocess

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def find_file_recursive(directory, filename):
    """ Tìm kiếm file theo tên đệ quy trong thư mục """
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def merge_all():
    media_dir = "media"
    voiceover_dir = "voiceover"
    output_dir = os.path.join("output", "merged")
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(voiceover_dir):
        print(f"❌ Thư mục '{voiceover_dir}' không tồn tại. Vui lòng chạy sinh voiceover trước!")
        return

    # Quét tất cả các file audio mp3
    mp3_files = sorted([f for f in os.listdir(voiceover_dir) if f.endswith(".mp3")])
    if not mp3_files:
        print("❌ Không tìm thấy file thuyết minh .mp3 nào!")
        return

    print("🎬 --- GHÉP ÂM THANH VÀO VIDEO TỪNG SCENE ---")
    for mp3_name in mp3_files:
        # Ví dụ: scene_05.mp3 -> tìm video có tên Scene05...mp4 hoặc khớp theo số thứ tự
        scene_num = mp3_name.split("_")[1].split(".")[0] # "05"
        
        # Tìm file video mp4 tương ứng trong thư mục media
        video_path = None
        for root, dirs, files in os.walk(media_dir):
            for f in files:
                # Kiểm tra xem tên file video có chứa số thứ tự scene không (ví dụ: Scene05_...mp4)
                if f.endswith(".mp4") and f"Scene{scene_num}" in f:
                    video_path = os.path.join(root, f)
                    break
            if video_path:
                break

        if not video_path:
            # Thử tìm kiếm theo định dạng class thông thường, ví dụ: Scene_05.mp4
            for root, dirs, files in os.walk(media_dir):
                for f in files:
                    if f.endswith(".mp4") and f"scene_{scene_num}" in f.lower():
                        video_path = os.path.join(root, f)
                        break
                if video_path:
                    break

        if not video_path:
            print(f"⚠️  Không tìm thấy video tương ứng cho {mp3_name} (Scene {scene_num}), bỏ qua.")
            continue

        audio_path = os.path.join(voiceover_dir, mp3_name)
        output_path = os.path.join(output_dir, f"scene_{scene_num}_merged.mp4")

        print(f"🔄 Đang ghép: {os.path.basename(video_path)} + {mp3_name} -> {os.path.basename(output_path)}")
        
        # Lệnh ffmpeg ghép audio và video
        # -c:v copy: copy trực tiếp stream video không encode lại để tiết kiệm thời gian
        # -c:a aac: encode audio sang aac
        # -shortest: kết thúc file khi luồng ngắn nhất kết thúc (thường là video hoặc audio)
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            output_path
        ]
        
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                print(f"❌ Lỗi khi ghép {mp3_name}: {result.stderr}")
            else:
                print(f"  ✅ Thành công!")
        except FileNotFoundError:
            print("❌ Không tìm thấy lệnh 'ffmpeg' trên hệ thống. Vui lòng cài đặt FFmpeg trước!")
            return
        except Exception as e:
            print(f"❌ Lỗi không xác định: {e}")

if __name__ == "__main__":
    merge_all()
