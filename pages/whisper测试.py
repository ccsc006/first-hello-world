from openai import OpenAI

# 设置OpenAI客户端
client = OpenAI()

audio_file = open("E:\\3两融业务\\低于130录音\\10100019732岳凯-20200325.wav", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
    # language="zh"  # 指定语言为中文
)
print(transcript)