import asyncio
import edge_tts  # pip install edge-tts==6.1.3
import os
from playsound import playsound  # 音频播放 pip install playsound==1.2.2
# audio_file, vtt_file当做变量传入
"""
在代码中，audio_file和vtt_file是非默认参数，voice、rate和volume具有默认值。
要解决此问题，需要对参数进行重新排序，以便非默认参数位于默认参数之前
"""
# 定义一个函数名为 txt_mp3_subtitles，它接受两 non-default arguments followed by three default arguments, and then two more non-default arguments.
def txt_mp3_subtitles(txt, audio_file, vtt_file, voice="zh-CN-XiaoxiaoNeural", rate="+0%", volume="+0%"):

    # 如果音频文件已经存在，删除它
    if os.path.exists(audio_file):
        os.remove(audio_file)

    # 定义一个异步函数名为 generate_speech，它接受五个参数：texts, voices, rates, volumes, out_file
    async def generate_speech(texts, voices, rates, volumes, out_file):
        # 使用 edge_tts 创建一个 communicate 对象，传入 texts, voices, rate, volume 参数
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

        # 以 utf-8 编码的方式写入字幕文件
        with open(vtt_file, "w", encoding="utf-8") as file:
            file.write(submaker.generate_subs())

    # 创建一个新的事件循环对象，并赋值给 loop 变量
    loop = asyncio.new_event_loop()

    # 使用 try-except-finally 块来处理可能发生的异常和清理工作
    try:
        # 设置当前线程的事件循环为 loop 对象
        asyncio.set_event_loop(loop)
        # 在 loop 对象上运行 generate_speech 函数，传入 txt, audio_file, vtt_file, voice, rate, volume 参数，并等待其完成
        loop.run_until_complete(generate_speech(txt, voice, rate, volume, audio_file))
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

#
# if __name__ == '__main__':
#     # 把文字变语音并进行播放
#     speak_text = "床前明月光，疑似地上霜。举头望明月，低头思故乡"
#     AUDIO_FILE = "txt_to_audio.mp3"
#     VTT_FILE = "txt_to_audio.vtt"
#     txt_mp3_subtitles(speak_text, audio_file=AUDIO_FILE, vtt_file=VTT_FILE)  # 把文字转换成mp3
