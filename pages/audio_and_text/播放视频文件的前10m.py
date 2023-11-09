import streamlit as st
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# 读取视频文件
target_path = 'your_video.mp4'

# 定义剪切后的视频文件名
output_path = 'trimmed_video.mp4'

# 剪切前10秒
ffmpeg_extract_subclip(target_path, 0, 10, targetname=output_path)

# 打开剪切后的视频文件
video_file = open(output_path, 'rb')
video_bytes = video_file.read()

# 使用st.video函数播放视频
st.video(video_bytes)

# 关闭并删除剪切后的视频文件
video_file.close()
os.remove(output_path)
