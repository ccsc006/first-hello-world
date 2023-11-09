# -*- coding: UTF-8 -*-
import os,sys
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

import chardet

st.title("文字转成语音:star:")
st.write("上传文本文件转成语音mp3格式的文件。")

sys.path.append('C:\\streamlit\\pages\\audio_and_text')
from text_to_audio_gpt import txt_mp3_subtitles

target_directory = "C:\\streamlit\\download"
os.makedirs(target_directory, exist_ok=True)

txt = st.file_uploader("请上传文本文件", type=["txt"])

if txt is not None:
    txt_filename = os.path.join(target_directory, txt.name)
    with open(txt_filename, "wb") as txt_file:
        txt_file.write(txt.read())
        # st.write(txt_filename)  #文字内容放在网站上
    st.success(f"成功将TXT文件保存.")

    #判断文件编码
    with open(txt_filename, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)['encoding']
        st.write(f"文件编码格式为：{result}，以下是文本内容：")
        mp3_file = txt_filename[:-4] + '.mp3'
        vtt_file = txt_filename[:-4] + '.vtt'
    with open(txt_filename, "r" , encoding=result) as txt_file:
        txt_content = txt_file.read()
        # st.write(txt_content)
        # 创建两个按钮，用户可以选择其中一个

        st.write(txt_content)  #文字内容放在网站上
        button_choice = st.radio("请选择输出女声还是男声：", ("女声", "男声"))

        # 根据选择的按钮执行不同的操作
        if button_choice == "女声":
            st.write("您选择了女声")
            selected_voice = "female"  # 存储选择的声音为 "female"
            # 在这里执行按钮1的操作
        else:
            st.write("您选择了男声")
            selected_voice = "male"  # 存储选择的声音为 "male"
            # 在这里执行按钮2的操作
        if st.button("文字转MP3"):
            if selected_voice == "female":
                # 在这里执行使用女声的文字转MP3的操作
                st.write("执行女声的文字转MP3操作")
                txt_mp3_subtitles(txt_content, mp3_file, vtt_file,voice="zh-CN-XiaoxiaoNeural")
                # txt_mp3_subtitles(txt_content, mp3_file, vtt_file,voice="zh-CN-liaoning-XiaobeiNeural")
            elif selected_voice == "male":
                # 在这里执行使用男声的文字转MP3的操作
                st.write("执行男声的文字转MP3操作")
                # mp3_filename = 'txt_to_audio.mp3'  # 指定MP3文件名
                txt_mp3_subtitles(txt_content, mp3_file, vtt_file,voice="zh-CN-YunxiNeural")

            st.success(f"已经将文本转换为MP3，点击播放。")
            # mp3_filename='txt_to_audio.mp3'
            st.audio(mp3_file, format="audio/mp3")
        # 保存MP3文件到磁盘
        # with open(mp3_filename, "wb") as mp3_file:
        #     mp3_file.write(open(mp3_filename, "rb").read())
        # st.audio(mp3_filename, format="audio/mp3")
        # base_download_url = "http://10.8.50.31/"
        # converted_pdf_file = base_download_url +mp3_file
            # st.markdown(f"[:arrow_down: 下载文件文件]({converted_pdf_file})")