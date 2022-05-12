from nturl2path import url2pathname
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_player import st_player
from get_urls import get_top_six

def main():
    # streamlit code
    # create page
    st.set_page_config(layout="wide")
    st.image('gui/youtorial.png')
    st.markdown('#')
    # create sidebar to copy you-who-must-not-be-named :) 
    with st.sidebar:
        c1, c2 = st.columns((1,2))
        with c1:
            st.image('gui/icons/home.png')
            st.image('gui/icons/compass.png')
            st.image('gui/icons/github.png')
            st.image('gui/icons/playlist.png')
            st.markdown('#')
            st.markdown('#')
            st.markdown('#')
            st.image('gui/icons/library.png')
            st.image('gui/icons/history.png')
            st.image('gui/icons/watch.png')
            st.image('gui/icons/thumbs.png')

        with c2: 
            st.header('Home')
            st.header('About')
            st.header('[Github](https://github.com/parkergauthier/YouTorial)')
            st.header('Subscriptions')
            st.markdown('#')
            st.markdown('#')
            st.markdown('#')
            st.header('Library')
            st.header('History')
            st.header('Watch later')
            st.header('Liked videos')
    
    # create text entry box and return video ids using SQL query 
    input_query = st.text_input('Enter search:',value = '')
    query_ids = get_top_six(input_query)

    st.markdown('#')
    st.subheader("Based on our algorithm, these are your recommended tutorials:")    
    
    # paste video IDs with base youtube url 
    base_url = "https://www.youtube.com/watch?v="

    def paste_urls(query_ids):
        urls = []
        for i in range(len(query_ids)):
            url = base_url + f"{query_ids[i]}"
            urls.append(url)
        return urls
    
    top_urls = paste_urls(query_ids)
    default_urls = ['VOyg2LzNiOA', 'sCddrLwH-fc', '7rAOLvHX_-8', 'Z9amZgbxhaI', 'KJgtrEGYsTo', 'F6eAQvj_5qA']
    while len(top_urls) < 6:
        i = len(top_urls)
        filler_url = base_url + f"{default_urls[i]}"
        top_urls.append(filler_url)
        if i == 5:
            break
    
    # return recommended videos 
    col1, col2, col3 = st.columns(3)
    with col1:
        event = st_player(top_urls[0])
        st.write(event)
        event = st_player(top_urls[3])
        st.write(event)  
    with col2:
        event = st_player(top_urls[1])
        st.write(event)
        event = st_player(top_urls[4])
        st.write(event)
    with col3:
        event = st_player(top_urls[2])
        st.write(event)
        event = st_player(top_urls[5])
        st.write(event)

# to run: streamlit run gui/streamer.py
if __name__ == "__main__":
    main()