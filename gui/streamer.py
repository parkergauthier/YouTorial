from nturl2path import url2pathname
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_player import st_player

def main():
    base_url = "https://www.youtube.com/watch?v="

# SQL query once sentiment analysis is done...

# get top 5 ids of ranked results 
# query_ids = """
#     select top 5 VideoID
#     from youtube_ID    
# """
# needs to reutn below list of ids: 
    query_ids = ["ZJy1ajvMU1k", "LdE9u0-SwEY", "ITP6uA8AFto", "yOgQIEywEWg", "Fo9EbhLWW1s"]
    # paste video IDs with base youtube url 
    def get_urls(query_ids):
        urls = []
        for i in range(0,4):
            url = base_url + f"{query_ids[i]}"
            urls.append(url)
        return urls
    
    top_urls = get_urls(query_ids)

    st.title("YouTorial")
    st.write("Based on our algorithm, these are your top five recommended tutorials:")

    with st.container(): 
    # Embed top 5 youtube videos 
        for i in range(0,4):
            st_player(top_urls[i])

# to run: streamlit run gui/streamer.py
if __name__ == "__main__":
    main()