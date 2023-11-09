
# -*- coding: UTF-8 -*-
import os,sys
import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space
from aip import AipOcr  # pip install baidu-aip
from PIL import Image

st.title("百度api-图片中提取文字:heart: ")
st.write("使用百度api从图片提取文字。")

APP_ID = '38381552'
API_KEY = 'PdCsbVjXwSGLn7mIQLlbPund'
SECRET_KEY = 'U5LGidjAToCKKnlFGXMS4g9fCviAuUdZ'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 指定c盘上的目标目录
target_directory = "/mount/src/first-hello-world/pages/"
# 确保目标目录存在
os.makedirs(target_directory, exist_ok=True)
pic_file = st.file_uploader("请上传图片文件", type=["jpg", "png"])
if pic_file is not None:
    # st.write(txt_file.name)

    # 构造目标文件路径
    target_path = os.path.join(target_directory, pic_file.name)
    # 保存上传的word文件到目标路径
    with open(target_path, "wb") as f:
        f.write(pic_file.read())
    pic_filename = pic_file.name
    # st.success(f"成功将PDF文件保存到 {target_path}")
    st.success(f"成功将图片文件上传。")
    path = target_directory + pic_filename

    img = Image.open(path)
    st.image(img, caption="上传的图片", use_column_width=True)  # 显示图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def get_content():
    path = target_directory + pic_filename
    image = get_file_content(path)
    content = client.basicGeneral(image)
    # print(content['words_result'])
    image_content = ""
    for words in content['words_result']:
        image_content += words['words']
    return image_content


if 'pic_filename' in locals():  # Check if pic_filename is defined
    st.markdown="识别的结果如下："
    st.write(get_content())