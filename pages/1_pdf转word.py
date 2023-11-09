# -*- coding: UTF-8 -*-
import os,sys

import office
import streamlit as st


st.title("pdf转word:sunglasses:")
# add_vertical_space(2)
st.subheader("上传pdf文件转成word文件")
st.sidebar.header("pdf转word")
# 3. 上传pdf 文件
pdf = st.file_uploader("请上传PDF", type="pdf")
if pdf is not None:
    st.write(pdf.name)

    # 读取 pdf
    # pdf_reader = PdfReader(pdf)
    # text = ""
    # for page in pdf_reader.pages:
    #     text += page.extract_text()
    # st.write(text)
    #
    # st.write("这是pdf的内容。")
# 指定c盘上的目标目录
    target_directory = "C:\\streamlit\\upload"
# 确保目标目录存在
    os.makedirs(target_directory, exist_ok=True)
# 构造目标文件路径
    target_path = os.path.join(target_directory, pdf.name)
# 保存上传的PDF文件到目标路径
    with open(target_path, "wb") as pdf_file:
        pdf_file.write(pdf.read())

    # st.success(f"成功将PDF文件保存到 {target_path}")
    st.success(f"成功将PDF文件上传。")

    if st.button("转换为Word"):
        # 执行PDF到Word转换操作
        pdfname=pdf.name
        office.pdf.pdf2docx(file_path=r'C:\\streamlit\\upload\\' + pdfname ,
                                output_path=r'C:\\streamlit\\download')

        st.success("PDF文件已成功转换为Word文件")
        # 设置已转换的Word文件路径
        download_name = pdf.name[:-4]+'.docx'

        base_download_url = "http://10.8.50.39/"
        converted_word_file = base_download_url + download_name
        st.markdown(f"[:arrow_down: 下载已转换的Word文件]({converted_word_file})")