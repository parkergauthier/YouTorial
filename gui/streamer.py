import streamlit as st
from streamlit_player import st_player
from get_urls import get_top_six

def main():
    # streamlit code
    # create main page with YouTorial logo
    st.set_page_config(layout="wide")
    st.image('gui/icons/youtorial.png')
    st.markdown('#')
    # create sidebar with link to Github repo
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
    
    # create user search bar and return video ids from database
    input_query = st.text_input('Enter search:',value = '')
    query_ids = get_top_six(input_query)

    st.markdown('#')
    st.markdown('#')
    st.subheader('Based on our algorithm, these are your recommended tutorials:')    
    
    # paste returned video IDs with base youtube url 
    base_url = "https://www.youtube.com/watch?v="

    def paste_urls(query_ids):
        urls = []
        for i in range(len(query_ids)):
            url = base_url + f"{query_ids[i]}"
            urls.append(url)
        return urls
    
    top_urls = paste_urls(query_ids)
    default_urls = ['VOyg2LzNiOA', 'sCddrLwH-fc', '7rAOLvHX_-8', 'Z9amZgbxhaI', 'KJgtrEGYsTo', 'F6eAQvj_5qA']

    # create default (mainpage) videos to populate if less than 6 recommended videos (due to database sparcity)
    while len(top_urls) < 6:
        i = len(top_urls)
        filler_url = base_url + f"{default_urls[i]}"
        top_urls.append(filler_url)
        if i == 5:
            break
    
    # embed recommended videos in grid 
    col1, col2, col3 = st.columns(3)
    with col1:
        st_player(top_urls[0])
        st_player(top_urls[3])
    with col2:
        st_player(top_urls[1])
        st_player(top_urls[4])
    with col3:
        st_player(top_urls[2])
        st_player(top_urls[5])

# to run: streamlit run gui/streamer.py
if __name__ == "__main__":
    main()