import os
import pandas as pd
import json
import psycopg2
from metrics import get_metrics, extract_metrics
from comments_request import get_comments, clean_comments
from database import engine
from database import conn_query


# Setting Paths
API_BASE_DIR = "scraping"
API_KEY_PATH = os.path.join(API_BASE_DIR, "api_keys.json")
JSON_PATH_IN = os.path.join(API_BASE_DIR, "500_videos.json")
OUT_PATH_TEST = os.path.join(API_BASE_DIR, "testing.csv")

# Reading API Key
with open(API_KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys["Alice2_key"]

cur = conn_query.cursor()

def snowball(videos_num=100):

    cur.execute(f"select * from no_repeat_ids limit {videos_num}")
    i = 0
    for video in cur:
        i += 1
        video_id = send2sql([video[0]])
        print(f"{i} videos completed: {video_id[0]}")
        if i == videos_num:
            print("YAY! ALL DONE! :D")


def send2sql(videos_list):
    """Looping through videos from list to get metrics/comments and pushing them to sql"""
    for i in videos_list:

        # grabbing metrics
        metrics_dict_dirty = get_metrics(i, apiKey=api_key)
        try:
            metrics_dict = extract_metrics(metrics_dict_dirty)
        except:
            print(
                f"This video: [{videos_list[0]}] is unavalable, and has been coded with -9 in metrics"
            )
            metrics_dict = {
                "videoID": videos_list[0],
                "likes": -9,
                "comments": -9,
                "length": -9,
                "views": -9,
            }
        # creating df for metrics
        num_comments = int(metrics_dict["comments"])
        df_met = pd.Series(metrics_dict).to_frame().T

        # change type of views to int
        # df_met.views = df_met.views.astype(int)

        # sending df to SQL
        df_met.to_sql(con=engine, name="youtube_metrics", if_exists="append")

        # grabbing comments
        if num_comments > 0:
            comments_dicts = get_comments(i, apiKey=api_key)
            clean_comments_list = clean_comments(comments_dicts)
        else:
            print(f"The follwing video has no comments: [{metrics_dict['videoID']}] ")
            clean_comments_list = []

        # Creating df for comments
        video_string = [i] * len(clean_comments_list)
        df_comm = pd.DataFrame(
            list(zip(video_string, clean_comments_list)), columns=["videoID", "comment"]
        )

        # Sending df to SQL
        df_comm.to_sql(con=engine, name="youtube_comments", if_exists="append")

    return videos_list


def clean_sql(table, column):
    """converts sql columns with strings of numbers to numerics"""
    cur.execute(
        f"alter table {table} alter column {column} type numeric using cast({column} as numeric);"
    )


if __name__ == "__main__":
    snowball(5000)

