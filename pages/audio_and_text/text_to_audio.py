
# -*- coding: UTF-8 -*-
import asyncio
import edge_tts  # pip install edge-tts==6.1.3
import os
from playsound import playsound  # 音频播放 pip install playsound==1.2.2

# 定义两个常量，表示要保存的音频文件和字幕文件的路径
AUDIO_FILE = "txt_to_audio.mp3"
VTT_FILE = "txt_to_audio.vtt"


# 定义一个函数名为 txt_mp3_subtitles，它接受四个参数：txt, voice, rate, volume
def txt_mp3_subtitles(txt, voice="zh-CN-XiaoyiNeural", rate="+0%", volume="+0%",):
    """
    将文本转换为音频文件和字幕文件，并保存到指定的路径
    :param txt: 要转换的文本
    :param voice: 要使用的语音，可以是 edge_tts 支持的任何语音
    :param rate: 语音的速度，可以是正负百分比
    :param volume: 语音的音调，可以是正负百分比
    :return: 如果转换和保存成功，返回 True，否则返回 False
    """
    AUDIO_FILE = "txt_to_audio.mp3"
    VTT_FILE = "txt_to_audio.vtt"
    # 如果音频文件已经存在，删除它
    if os.path.exists(AUDIO_FILE):
        os.remove(AUDIO_FILE)

    # 定义一个异步函数名为 generate_speech，它接受五个参数：texts, voices, rates, volumes, out_file
    async def generate_speech(texts, voices, rates, volumes, out_file):
        # 使用 edge_tts创建一个 communicate 对象，传入 texts, voices, rate, volume 参数
        communicate = edge_tts.Communicate(texts, voices, rate=rates, volume=volumes)

        # 使用 edge_tts 创建一个 submaker 对象，用于生成字幕
        submaker = edge_tts.SubMaker()

        # 使用一个上下文管理器，以二进制写入模式打开音频文件，并获文件对象
        with open(out_file, "wb") as file:
            # 使用异步迭代器遍历 communicate 对象返回的数据块
            async for chunk in communicate.stream():
                # 如果数据块的类型是 audio，表示是音频数据，将其写入到文件中
                if chunk["type"] == "audio":
                    file.write(chunk["data"])
                # 如果数据块的类型是 WordBoundary，表示是单词信息，将其添加到 submaker 对象中
                elif chunk["type"] == "WordBoundary":
                    submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

        # 以 utf-8 编码 的方式写入字幕文件
        with open(VTT_FILE, "w", encoding="utf-8") as file:
            file.write(submaker.generate_subs())

    # 创建一个新的事件循环对象，并赋值给 loop 变量
    loop = asyncio.new_event_loop()

    # 使用 try-except-finally 块来处理可能发生的异常和清理工作
    try:
        # 设置当前线程的事件循环为 loop 对象
        asyncio.set_event_loop(loop)
        # 在 loop 对象上运行 generate_speech 函数，传入 txt, voice, rate, volume, AUDIO_FILE 参数，并等待其完成
        loop.run_until_complete(generate_speech(txt, voice, rate, volume, AUDIO_FILE))
        # 关闭 loop 对象
        loop.close()
    except Exception as e:
        # 打印异常信息
        print(f"语音合成出错：{e}")
        # 关闭 loop 对象
        loop.close()
        # 返回 False 表示语音合成失败
        return False

    # 返回 True 表示语音合成成功
    return True


# 获取嗓音
def get_voices():
    import requests
    voice_list_url = "https://speech.platform.bing.com/consumer/speech/synthesize/readaloud/voices/list?trustedclienttoken=6A5AA1D4EAFF4E9FB37E23D68491D6F4"
    voices = requests.get(voice_list_url).json()

    for voice in voices:
        if 'zh-CN' in voice["Locale"]:
            print(voice)
            print(voice.get('ShortName'))


if __name__ == '__main__':
    # 把文字变语音并进行播放
    speak_text = "C:\\python-50auto\\streamlit-web\\download\\11.txt"

    # speak_text = "床前明月光，疑似地上霜。举头望明月，低头思故乡"
    txt_mp3_subtitles(speak_text)  # 把文字转换成mp3
    # txt_mp3_subtitles(speak_text , voice = "zh-CN-YunjianNeural" )  # 换嗓音
    # playsound(AUDIO_FILE)  # 播放mp3语音文件

    # 获取可以使用的嗓音
    # get_voices()

        # zh - CN - XiaoxiaoNeural  标准女生
        # zh - CN - XiaoyiNeural
        # zh - CN - YunjianNeural
        # zh - CN - YunxiNeural
        # zh - CN - YunxiaNeural
        # zh - CN - YunyangNeural
        # zh - CN - liaoning - XiaobeiNeural
        # zh - CN - shaanxi - XiaoniNeural