import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import pickle
import os
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


st.header("Ask for PDF")

# 3. 上传pdf 文件
pdf = st.file_uploader("请上传PDF:ok_hand:", type="pdf")
if pdf is not None:
    st.write(pdf.name)
    # 读取 pdf
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    # st.write(text)
    # 4. 对文本进行切割 data connection
    # chunk_size 指定切割文件块的大小
    # chunk_overlap 指定文件块之间的覆盖字符数
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)
    # st.write(chunks)
    store_name = pdf.name[:-4]
    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            vectorStore = pickle.load(f)
        st.write("嵌入已经从磁盘加载好了")
    else:
        # 5. 对切割之后的文件进行向量化，存储到向量数据库中
        # embedding
        embeddings = OpenAIEmbeddings()
        vectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        # 6. 对向量数据库进行持久化
        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(vectorStore, f)
        st.write("向量嵌入完成")

    # 7. 用户输入，搜索向量数据库，返回结果。
    query = st.text_input("请输入与PDF相关的问题！")
    if query:
        docs = vectorStore.similarity_search(query=query, k=1)
        llm = OpenAI(model_name="gpt-3.5-turbo")
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)

        st.write(response)
        st.write(cb)  # 花了多少钱