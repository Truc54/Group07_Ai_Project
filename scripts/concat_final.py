import os
import sys
import subprocess

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def concat_all_videos():
    merged_dir = os.path.join("output", "merged")
    final_output = os.path.join(merged_dir, "FINAL_VIDEO.mp4")
    list_file_path = "temp_concat_list.txt"

    if not os.path.exists(merged_dir):
        print(f"❌ Thư mục '{merged_dir}' không tồn tại. Vui lòng chạy merge_audio_video.py trước!")
        return

    # Lọc và sắp xếp các file đã ghép tiếng theo thứ tự scene
    merged_files = [f for f in os.listdir(merged_dir) if f.endswith("_merged.mp4") and f.startswith("scene_")]
    if not merged_files:
        print("❌ Không tìm thấy file video đã ghép tiếng (*_merged.mp4) nào trong thư mục output/merged/!")
        return

    # Sắp xếp theo số thứ tự của scene (ví dụ: scene_01_merged.mp4 -> 1)
    def extract_scene_num(filename):
        try:
            return int(filename.split("_")[1])
        except:
            return 999

    merged_files.sort(key=extract_scene_num)

    print(f"🔗 Tìm thấy {len(merged_files)} scene đã ghép âm thanh. Đang lập danh sách nối...")
    
    # Tạo file danh sách tạm thời cho FFmpeg concat
    try:
        with open(list_file_path, "w", encoding="utf-8") as f:
            for filename in merged_files:
                abs_path = os.path.abspath(os.path.join(merged_dir, filename))
                # FFmpeg concat yêu cầu định dạng: file 'đường_dẫn_tuyệt_đối'
                # Cần thay thế dấu gạch chéo ngược trên Windows để tránh lỗi
                formatted_path = abs_path.replace("\\", "/")
                f.write(f"file '{formatted_path}'\n")
        
        print("🚀 Đang tiến hành nối các file video thành video cuối cùng...")
        
        # Chạy lệnh ffmpeg concat copy trực tiếp (không re-encode nên cực kỳ nhanh và không giảm chất lượng)
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", list_file_path,
            "-c", "copy",
            final_output
        ]
        
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"❌ Lỗi khi nối video: {result.stderr}")
        else:
            print(f"🎉 THÀNH CÔNG! Video hoàn chỉnh đã được xuất ra tại: {final_output}")
            
    except FileNotFoundError:
        print("❌ Không tìm thấy lệnh 'ffmpeg' trên hệ thống. Vui lòng cài đặt FFmpeg trước!")
    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
    finally:
        # Xóa file danh sách tạm thời
        if os.path.exists(list_file_path):
            os.remove(list_file_path)

if __name__ == "__main__":
    concat_all_videos()
