import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import socket
st.set_page_config(
    page_title="北京分公司",
    page_icon="👋",
)

st.write("# 欢迎使用 本网站! 👋")

st.sidebar.success("在上方选择一个功能。")
add_vertical_space(4)
st.write("这个网站是用**Streamlit** 构建的开源应用框架。")
add_vertical_space(2)
st.write("目前有pdf转word、文字转语言、语音转文字等功能。")
add_vertical_space(2)
st.write("**👈 从侧边栏选择一个功能**，看看 Streamlit 能做什么吧！")












