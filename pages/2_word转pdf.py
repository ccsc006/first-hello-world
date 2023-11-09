# -*- coding: UTF-8 -*-
import os,sys

import office
import streamlit as st
import pythoncom

from streamlit_extras.add_vertical_space import add_vertical_space


st.title("word转pdf:smile: ")
add_vertical_space(2)
st.subheader("上传word文件转成pdf文件")

# 3. 上传docx 文件
docx = st.file_uploader("请上传WORD", type="docx")
if docx is not None:
    st.write(docx.name)
    # 指定c盘上的目标目录
    target_directory = "C:\\streamlit\\upload"
    # 确保目标目录存在
    os.makedirs(target_directory, exist_ok=True)
    # 构造目标文件路径
    target_path = os.path.join(target_directory, docx.name)
    # 保存上传的word文件到目标路径
    with open(target_path, "wb") as word_file:
        word_file.write(docx.read())
    word_file=word_file.name
    # st.success(f"成功将PDF文件保存到 {target_path}")
    st.success(f"成功将word文件上传。")

    if st.button("转换为PDF"):
        print(word_file)
        pythoncom.CoInitialize()  # 初始化COM
        download_name = docx.name[:-5] + '.pdf'

        # 'C:\\python-50auto\\streamlit-web\\upload\\' + word_file
        office.word.docx2pdf(path=r''+word_file,
                     output_path=r'C:\\streamlit\\download')
        st.success("WORD文件已成功转换为PDF文件")

        pythoncom.CoUninitialize()  # 在程序结束时清理
        # 设置已转换的Word文件路径

        base_download_url = "http://10.8.50.39/"
        converted_pdf_file = base_download_url + download_name
        print(converted_pdf_file)
        st.markdown(f"[:arrow_down: 下载已转换的pdf文件]({converted_pdf_file})")