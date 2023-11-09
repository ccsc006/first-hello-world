import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import get_openai_callback
# 设置OpenAI API密钥

_ = load_dotenv(find_dotenv())

# openai.api_key  = os.getenv('RAW_OPENAI_API_KEY')
openai.api_key  = os.getenv('OPENAI_API_KEY')

# 创建Streamlit应用标题
st.title("Chat with ZSZQ-3:star:")

# 创建一个输入框，允许用户输入问题
user_input = st.text_input("请输入你的问题:")

# 当用户提交问题时执行以下操作
if user_input:
    # 将用户输入添加到消息列表
    messages = [{"role": "user", "content": user_input}]

    # 调用OpenAI的ChatCompletion模型
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # 提取GPT-3的回复
    bot_reply = completion.choices[0].message.content

    # 显示GPT-3的回复
    st.write("ZSZQ-3回复:", bot_reply)
    st.write("本次花费token数量为：",str(completion.usage.total_tokens))




