import os
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
OUT_PATH_TEST = os.path.join(API_BASE_DIR, "testing.csv")

# Reading API Key
with open(API_KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys["John_key"]

# Reading in sample JSON, to be changed with real video list later
####################
# with open(JSON_PATH_IN, "r") as f:
#     videos = json.load(f)

conn = psycopg2.connect(
    dbname="youtube-content",
    user="youtube-project",
    host="35.226.197.36",
    password="Zhanghaokun_6",
)

cur = conn.cursor()

cur.execute(
    """ select * from test_table_unique where "videoID" not in (select "videoID" from youtube_content) """
)

records = cur.fetchall()
cur.close()

records = video_list

# videos_list = [
#     "SwSbnmqk3zY",
#     videos["videoID"]["1"],
#     videos["videoID"]["2"],
#     videos["videoID"]["3"],
#     videos["videoID"]["4"],
# ]
#####################


def send2sql(videos_list):
    """Looping through videos from list to get metrics/comments and pushing them to sql"""
    for i in videos_list:

        # grabbing comments
        comments_dicts = get_comments(i, apiKey=api_key)
        clean_comments_list = clean_comments(comments_dicts)

        # Creating df for comments
        video_string = [i] * len(clean_comments_list)
        df_comm = pd.DataFrame(
            list(zip(video_string, clean_comments_list)), columns=["videoID", "comment"]
        )

        # Sending df to SQL
        df_comm.to_sql(con=conn, name="youtube_comments", if_exists="append")

        # grabbing metrics
        metrics_dict_dirty = get_metrics(i, apiKey=api_key)
        metrics_dict = extract_metrics(metrics_dict_dirty)

        # creating df for metrics
        df_met = pd.Series(metrics_dict).to_frame().T

        # sending df to SQL
        df_met.to_sql(con=conn, name="youtube_metrics", if_exists="append")


if __name__ == "__main__":
    send2sql(["k_36JKMLp08"])
