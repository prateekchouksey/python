# install streamlit and pytube -- pip install streamlit pyt
import streamlit as st
import yt_dlp

st.title("🎬 YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL:")

if st.button("Download Video") and url:
    try:
        yt_op = {
            'format': 'mp4',  # Avoid merging by picking a compatible single stream
            'merge_output_format': 'mp4',  # Just to be safe
            'postprocessors': [],  # Disable post-processing
        }

        with yt_dlp.YoutubeDL(yt_op) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            st.success(f"✅ Download completed: {title}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

        
st.markdown("### 👨‍💻 Developed by: PRATEEK CHOUKSEY")
      


