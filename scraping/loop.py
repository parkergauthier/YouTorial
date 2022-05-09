
import os
from matplotlib.cbook import flatten
import googleapiclient.discovery
import pandas as pd
import json
from sqlalchemy import create_engine

from sqlalchemy import values
from metrics import get_metrics, extract_metrics
from random import sample
from comments_request import get_comments, clean_comments

# Connecting to DB
conn_string = "postgresql://youtube-project:Zhanghaokun_6@35.226.197.36/youtube-content"
db = create_engine(conn_string)
conn = db.connect()



# Setting Paths
API_BASE_DIR = "scraping"
API_KEY_PATH = os.path.join(API_BASE_DIR, "api_keys.json")
JSON_PATH_IN = os.path.join(API_BASE_DIR, "500_videos.json")
OUT_PATH_TEST = os.path.join(API_BASE_DIR,"testing.csv")

# Reading API Key
with open(API_KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys['John_key']

# Reading in sample JSON, to be changed with real video list later
####################
with open(JSON_PATH_IN, "r") as f:
    videos = json.load(f)

videos_list = ["SwSbnmqk3zY", videos['videoID']['1'],
               videos['videoID']['2'], videos['videoID']['3'], videos['videoID']['4']]
#####################

list_comments = []
list_metrics = []

comment_dict = {}
for i in videos_list:
    comments_dicts = get_comments(i, apiKey=api_key)['items']
    clean_comments_list = clean_comments(comments_dicts)

    video = i

    video_string = [video]*len(clean_comments_list)

    df = pd.DataFrame(list(zip(video_string, clean_comments_list)), columns=["videoId", "comment"])
    df.to_sql(con=conn, name="youtube_comment", if_exists="append")

