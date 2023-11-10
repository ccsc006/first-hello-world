# -*- coding: UTF-8 -*-
import os,sys
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from dotenv import load_dotenv, find_dotenv
import openai

sys.path.append('/mount/src/first-hello-world/pages/audio_and_text')
from audio_to_text import transcribe_audio

# _ = load_dotenv(find_dotenv())
# openai.api_key  = os.getenv('OPENAI_API_KEY')

# 设置OpenAI API密钥
openai.api_key = "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"
st.title("mp3转文字:fire:")
st.write("上传mp3文件转成文字。")
target_directory = "/mount/src/first-hello-world/pages/"
os.makedirs(target_directory, exist_ok=True)

mp3 = st.file_uploader("请上传MP3文件", type=["mp3",'wav'])

if mp3 is not None:
    mp3_filename = os.path.join(target_directory, mp3.name)
    with open(mp3_filename, "wb") as mp3_file:
        mp3_file.write(mp3.read())
    st.success(f"成功将MP3文件保存.")

    if st.button("mp3转文字"):
        mp3_filename = os.path.join(target_directory, mp3.name)
        audio_file_path = mp3_filename# 跟脚本存同一个路径下的mp3音频文件
        res1 = transcribe_audio(audio_file_path, response_format='text')
        res = transcribe_audio(audio_file_path, response_format='srt')  # 创建字幕文件
        st.write(res1)

        mp3_txt=mp3_filename[:-4] + '.txt'
        with open(mp3_txt, 'w',encoding='utf-8') as f:
            f.write(res1)

        