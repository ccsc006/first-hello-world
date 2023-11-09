import streamlit as st
import time

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"
col1,col2,col3 = st.columns([1,2,1])

col1.markdown(" # welcome to my app!")
col1.markdown(" here is some info on the app")

def change_photo_state():
    st.session_state["photo"] = "done"

uploaded_photo=col2.file_uploader("upload a photo",on_change=change_photo_state)
camera_photo=col2.camera_input("take a photo",on_change=change_photo_state)

if st.session_state["photo"]=="done":
    progress_bar=col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    col2.success("photo uploaded successfully!")

    col3.metric(label="Temperature",value="60",delta="3")

    with st.expander("click to read more"):
        st.write("hello,here are more details on this topic that you were interested in.")
        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)