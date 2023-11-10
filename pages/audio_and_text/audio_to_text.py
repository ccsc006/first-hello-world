import logging
import openai

# 定义一个名为 transcribe_audio 的函数，它接受两个参数：audio_file 和 response_format
def transcribe_audio(audio_file, response_format) -> str:
    openai.api_key = "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"
    """
    使用 whisper 模型将音频文件转录为文字，并以指定的格式返回转录结果。
    :param audio_file: 要转录的音频文件的路径
    :param response_format: 转录结果的格式，可以是 json、text、srt、vtt、verbose_json 之一
    :return: 转录结果作为一个字符串，或者如果发生错误则返回一个空字符串
    """

    # 使用一个 try-except 块来处理可能发生的 openai API 的错误
    try:
        # 使用一个上下文管理器，以二进制模式打开音频文件对象。
        with open(audio_file, "rb") as audio_file:
            # 调用 openai.Audio.transcribe 方法，传入音频文件对象、和转录格式
            transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format=response_format)
            # 返回转录结果内容
            return transcript
    except openai.error.OpenAIError as e:
        # 使用 logging.error 方法记录错误信息，并包含 e 的值
        logging.error(f"转录音频失败: {e}")
        # 返回一个空字符串
        return ""


if __name__ == '__main__':
    audio_file_path = 'txt_to_audio.mp3' # 跟脚本存同一个路径下的mp3音频文件
    res1 = transcribe_audio(audio_file_path, response_format='text')
    res = transcribe_audio(audio_file_path, response_format='srt')  #创建字幕文件
    print(res1) # 具体音频总说话的文本内容

    with open("十年.srt", 'w') as f:
        f.write(res)