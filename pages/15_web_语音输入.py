import streamlit as st
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


def record_audio(duration=5, sample_rate=44100, channels=2, device=None):
    st.write("录制中...")
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels, dtype=np.int16,
                        device=device)
    sd.wait()
    st.write("录制完成!")
    return audio_data, sample_rate


def save_audio(audio_data, filename, format="wav"):
    audio_segment = AudioSegment(
        audio_data.tobytes(),
        frame_rate=audio_data.shape[0],
        sample_width=audio_data.dtype.itemsize,
        channels=audio_data.shape[1]
    )
    audio_segment.export(filename, format=format)


def main():
    st.title("录制音频并保存")

    # 查询可用的音频输入设备
    devices = sd.query_devices()
    device_names = [device["name"] for device in devices]

    # 在界面上显示可用的设备
    selected_device = st.selectbox("选择音频输入设备", device_names)

    duration = st.slider("录制时长（秒）", min_value=1, max_value=10, value=5)
    format_option = st.selectbox("保存格式", ["wav", "mp3"])

    if st.button("开始录制"):
        # 获取选定设备的ID
        device_id = device_names.index(selected_device)
        audio_data, sample_rate = record_audio(duration=duration, device=device_id)
        st.audio(audio_data, format="audio/wav", sample_rate=sample_rate)

        if st.button("保存音频"):
            filename = st.text_input("输入文件名（不包括文件扩展名）", "output")
            full_filename = f"{filename}.{format_option}"
            save_audio(audio_data, full_filename, format=format_option)
            st.success(f"音频已保存为 {full_filename}")


if __name__ == "__main__":
    main()
