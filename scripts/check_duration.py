import os
import sys
from pydub import AudioSegment

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_all_durations():
    voiceover_dir = "voiceover"
    if not os.path.exists(voiceover_dir):
        print(f"❌ Thư mục '{voiceover_dir}' không tồn tại. Vui lòng chạy sinh voiceover trước!")
        return

    mp3_files = sorted([f for f in os.listdir(voiceover_dir) if f.endswith(".mp3")])
    if not mp3_files:
        print("❌ Không tìm thấy file .mp3 nào trong thư mục voiceover!")
        return

    print("🎙️ --- THỜI LƯỢNG CÁC FILE THUYẾT MINH ---")
    total_duration = 0.0
    for file in mp3_files:
        path = os.path.join(voiceover_dir, file)
        try:
            audio = AudioSegment.from_file(path)
            duration = len(audio) / 1000.0  # chuyển từ ms sang s
            total_duration += duration
            print(f"🔹 {file}: {duration:.2f} giây")
        except Exception as e:
            print(f"❌ Lỗi khi đọc file {file}: {e}")

    minutes = int(total_duration // 60)
    seconds = total_duration % 60
    print("----------------------------------------")
    print(f"📊 Tổng thời lượng thuyết minh: {total_duration:.2f} giây (~{minutes} phút {seconds:.1f} giây)")

if __name__ == "__main__":
    check_all_durations()
