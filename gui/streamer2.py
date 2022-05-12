from nturl2path import url2pathname
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_player import st_player


def main():
    # streamlit code
    st.set_page_config(layout="wide")
    st.image('gui/youtorial.png')
    st.markdown('#')
    st.markdown('#')
    with st.sidebar:
        c1, c2 = st.columns((1,2))
        with c1:
            st.image('gui/icons/menu.png')
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
            st.header('#')
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
    
    # dropdown list of example queries for presentation
    search = st.selectbox('Enter query', queries)
    queries = ['How to draw sonic the hedgehog', 'How to fry an egg', 'How to code in Python', 'How to make salsa']
    ## SQL queries
    sonic_ids = '
    '
    egg_ids = '
    '
    python_ids = '
    '
    salsa_ids = '
    '

    # grab video ids of corresponding dropdown selection 
    if search == queries[0]:
        query_ids = sonic_ids
    if search == queries[1]:
        query_ids = egg_ids
    if search == queries[2]:
        query_ids = python_ids
    if search == queries[3]:
        query_ids = salsa_ids   
    
    st.markdown('#')
    st.subheader("Based on our algorithm, these are your recommended tutorials:")    
    
    # paste video IDs with base youtube url 
    base_url = "https://www.youtube.com/watch?v="

    def paste_urls(query_ids):
        urls = []
        for i in range(0,6):
            url = base_url + f"{query_ids[i]}"
            urls.append(url)
        return urls
    
    top_urls = paste_urls(query_ids)

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