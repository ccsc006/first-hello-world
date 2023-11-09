# -*- coding: UTF-8 -*-
import os,sys
import io
import time

import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from moviepy.editor import *

st.title("从视频中提取MP3:rocket:")
st.write("从MP4视频文件中提取MP3背景声音。")
mp4_file = st.file_uploader("请上传图片文件", type=["mp4"])
if mp4_file is not None:
    # st.write(txt_file.name)
    # 指定c盘上的目标目录
    target_directory = "/mount/src/first-hello-world/pages/"
    dw_directory = "/mount/src/first-hello-world/pages/"
    # 确保目标目录存在
    os.makedirs(target_directory, exist_ok=True)
    # 构造目标文件路径
    target_path = os.path.join(target_directory, mp4_file.name)
    # 保存上传的word文件到目标路径
    with open(target_path, "wb") as f:
        f.write(mp4_file.read())
    mp4_file = mp4_file.name

    st.success(f"成功将视频文件上传。")

    # 打开视频文件
    video_file = open(target_path, 'rb')
    video_bytes = video_file.read()
    # 使用st.video函数播放视频
    st.video(video_bytes)

    if st.button("提取mp3文件"):
        # 创建一个进度条组件
        progress_bar = st.progress(0)
        # 创建一个空文本容器
        progress_text = st.empty()
        # 模拟一个耗时任务
        for i in range(101):
            # 更新进度条的值
            progress_bar.progress(i)
            # 在任务的适当位置执行音频文件的转换和保存
            if i == 50:

                path = target_directory + mp4_file
                mp3_file = mp4_file[:-4] + '.mp3'
                dw_path = dw_directory + mp3_file
                video = VideoFileClip(path)
                video.audio.to_audiofile(dw_path)
            # 模拟任务的耗时
            time.sleep(0.1)
            # 在每次迭代中用新文本替换文本容器
            progress_text.text(f"任务进度: {i}%")
        # 完成任务后更新进度条为100%
        progress_bar.progress(100)

        st.success(f"已提取到MP3，点击播放。")
        mp3_filename = mp4_file[:-4] + '.mp3'

        print(mp3_filename)
        mp3_filename = dw_directory + mp3_filename
        st.audio(mp3_filename, format="audio/mp3")