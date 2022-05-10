from nturl2path import url2pathname
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_player import st_player
from streamlit_player import st_player, _SUPPORTED_EVENTS
from streamlit_gallery.utils.readme import readme


base_url = "https://www.youtube.com/watch?v="

# get top 5 ids of ranked results 
query_ids = """
    select top 5 VideoID
    from youtube_ID    
"""

get_urls(query_ids):
    url1 = base_url + f"{query_ids[0]}"
    url2 = base_url + f"{query_ids[1]}"
    url3 = base_url + f"{query_ids[2]}"
    url4 = base_url + f"{query_ids[3]}"
    url5 = base_url + f"{query_ids[4]}"
    return(list(url1, url2, url3, url4, url5))

with st.container():
    
def main():
    st.title("YouTorial")
    st.write("Based on our algorithm, these are your top five recommended tutorials")

    col1, col2, col3, col4, col5 = st.beta_columns(5)
    # Embed a youtube video
    for (i in get_urls(query_ids)): 
        st_player(i)


# to run: streamlit run gui/streamer.py
if __name__ == "__main__":
    main()