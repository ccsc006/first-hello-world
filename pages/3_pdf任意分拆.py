import os,io
import PyPDF2
import office
import streamlit as st
import pythoncom
import sys
from PyPDF2 import PdfReader, PdfWriter
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader

st.title("PDF按指定页任意分拆:thumbsup:")
st.write("想拆几页拆几页。")
st.subheader("选择一个PDF文件并指定要分拆的页数范围")

# 上传PDF文件
pdf_file = st.file_uploader("请上传PDF文件", type=["pdf"])

if pdf_file is not None:

    # 读取上传的PDF文件的内容到内存中
    pdf_content = pdf_file.read()

    # 使用 PyPDF2 获取页数
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
    num_pages = len(pdf_reader.pages)

    st.write(f"已上传的PDF文件 '{pdf_file.name}' 有  {num_pages} 页。")

# 输入框和按钮，用于指定起始页数和结束页数
    start_page = st.number_input("起始页数", min_value=1, value=1)
    end_page = st.number_input("结束页数", min_value=start_page, value=num_pages)

    # 检查用户是否点击了分拆按钮
    if st.button("分拆为新的PDF"):
        # 读取上传的PDF文件

        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # 创建一个新的PDF文件对象
        pdf_writer = PyPDF2.PdfWriter()
        # 分拆页数范围内的页
        for page_number in range(start_page - 1, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_number])

        # 构建新的PDF文件名
        new_pdf_filename = f"split_{start_page}-{end_page}_{pdf_file.name}"
        # 指定目标目录
        target_directory = "C:\\streamlit\\download\\"
        target_path = os.path.join(target_directory, new_pdf_filename)
        # 保存新的PDF文件
        with open(target_path, "wb") as new_pdf_file:
            pdf_writer.write(new_pdf_file)

        # 提供下载链接
        st.success(f"已成功分拆并保存为 {new_pdf_filename}")
        base_download_url = "http://10.8.50.39/"
        converted_pdf_file = base_download_url + new_pdf_filename

        st.markdown(f"[:arrow_down: 下载已转换的pdf文件]({converted_pdf_file})")
