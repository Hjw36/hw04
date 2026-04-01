import whisper
from whisper.utils import get_writer

# 加载small模型，平衡精度与速度
model = whisper.load_model("small")

# 音频路径（WSL格式，对应D盘WSL_Code文件夹，注意拼写正确）
audio_path = "/mnt/d/WSL_Code/hw04_voice.mp3"

# 【关键修正】直接传音频路径，绝对不能加audio_path=！
result = model.transcribe(audio_path, language="zh")

# 打印识别结果
print("识别结果：")
print(result["text"])

# 输出目录（和音频同文件夹，拼写正确）
output_dir = "/mnt/d/WSL_Code/"

# 保存TXT文本
with open(f"{output_dir}asr_result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

# 保存SRT字幕
srt_writer = get_writer("srt", output_dir)
srt_writer(result, audio_path)

print("识别完成，结果已保存至D盘WSL_Code文件夹")