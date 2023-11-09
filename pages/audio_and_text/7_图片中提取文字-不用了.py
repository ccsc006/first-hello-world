# -*- coding: UTF-8 -*-
import os,sys
import io
import time
import PyPDF2
import office
import streamlit as st
import pythoncom

from PyPDF2 import PdfReader, PdfWriter
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader

import pytesseract
from PIL import Image
st.title("图片中提取文字:heart: ")
st.write("从图片中提取简体中文文字。")
txt_file = st.file_uploader("请上传图片文件", type=["jpg","png"])


if txt_file is not None:
    # st.write(txt_file.name)

    # 指定c盘上的目标目录
    target_directory = "C:\\streamlit\\upload\\"
    # 确保目标目录存在
    os.makedirs(target_directory, exist_ok=True)
    # 构造目标文件路径
    target_path = os.path.join(target_directory, txt_file.name)
    # 保存上传的word文件到目标路径
    with open(target_path, "wb") as f:
        f.write(txt_file.read())
    txt_file = txt_file.name
    # st.success(f"成功将PDF文件保存到 {target_path}")
    st.success(f"成功将图片文件上传。")
    path = target_directory + txt_file
    img = Image.open(path)
    st.image(img, caption="上传的图片", use_column_width=True)  # 显示图片

    if st.button("识别中文文字"):
        testdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
        # path = 'C:\python-50auto\streamlit-web\ocr测试.jpg'

        text = pytesseract.image_to_string(img, lang='chi_sim')
        st.write(text)