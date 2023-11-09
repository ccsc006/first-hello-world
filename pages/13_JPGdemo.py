import streamlit as st
import openai
import requests
import os
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv, find_dotenv
# 设置OpenAI API密钥
# openai.api_key = "YOUR_API_KEY"

_ = load_dotenv(find_dotenv())

# openai.api_key  = os.getenv('RAW_OPENAI_API_KEY')
openai.api_key  = os.getenv('OPENAI_API_KEY')

# 创建Streamlit应用标题
st.title("生成图像描述:smile:")

# 创建一个输入框，允许用户输入图像描述信息
prompt = st.text_input("请输入你想生成的图像的描述信息:")

# 当用户提交描述时执行以下操作
if st.button("生成图像"):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    st.image(image_url, use_column_width=True, caption="生成的图像")

    with open(f"./download/{prompt}.jpg", "wb") as f:
        f.write(requests.get(image_url).content)


    st.success("图像生成成功并保存在本地")

