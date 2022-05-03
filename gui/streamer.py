import streamlit as st
from streamlit_player import st_player

title = "How to change a tire..."
creator = "John Doe"
search = "how do I change a tire"

st.title("YouTorial")
st.write("Based on our algorithm, {title} by {creator} is the recommended tutorial for {search}")
# Embed a youtube video
st_player("https://youtu.be/CmSKVW1v0xM")


# to run: streamlit run gui/streamer.py
if __name__ == "__main__":
    st.title()
    st.write()
    st_player(topurl)