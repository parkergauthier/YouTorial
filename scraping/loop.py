
import os
import googleapiclient.discovery
from matplotlib.pyplot import axis
import pandas as pd
import json
import psycopg2
from sqlalchemy import values
from metrics import get_metrics, extract_metrics
from random import sample
from comments_request import get_comments, clean_comments
from sqlalchemy import create_engine

# function that call list of no_duplicated ID view in loop.py
conn_string="dbname='youtube-content', user='youtube-project', host='35.226.197.36', password='Zhanghaokdun_6'"

conn = psycopg2.connect(host='35.226.197.36', user = 'youtube-project', password = 'Zhanghaokun_6', database = 'youtube-content')
cur = conn.cursor()
cur.execute(""" SELECT * FROM test_table_unique_output WHERE "videoID" not in (select "videoID" from youtube_content); """)
records = cur.fetchall()
cur.close()



# Setting Paths
API_BASE_DIR = "C:/Users/Haokun Zhang/Desktop/github/YouTorial"
Scraping_path = os.path.join(API_BASE_DIR, "scraping")
API_KEY_PATH = os.path.join(Scraping_path, "api_keys.json")
JSON_PATH_IN = os.path.join(Scraping_path, "500_videos.json")


# Reading API Key
with open(API_KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys["John_key"]

# Reading in sample JSON, to be changed with real video list later
####################
with open(JSON_PATH_IN, "r") as f:
    videos = json.load(f)



videos_list = [
    "SwSbnmqk3zY",
    videos["videoID"]["1"]
#     videos["videoID"]["2"],
#     videos["videoID"]["3"],
#     videos["videoID"]["4"],
 ]
#####################

# list_comments = []
# list_metrics = []


<<<<<<< HEAD
# for i in videos_list:
#     comments_dicts = get_comments(i, apiKey=api_key)['items']
#     clean_comments_list = clean_comments(comments_dicts)
#     dict_comments = {
#         "videoId": i,
#         "comments": clean_comments_list
#     }

#     list_comments += [dict_comments]

#     # create a comment dataframe
#     df_comments = pd.DataFrame(list_comments)

#     # split the comments by ID
#     df_comments.comments.apply(pd.Series) \
#         .merge(df_comments, left_index = True, right_index = True) \
#         .drop(["comments"], axis=1) \
#         .melt(id_vars = ["videoId"], value_name = "comments") \
#         .drop("variable", axis = 1) \
#         .dropna()
# print(df_comments)
# #     metrics_dicts = get_metrics(i, apiKey=api_key)
# #     print(metrics_dicts)
# #     extract_metrics_list = extract_metrics(metrics_dicts)

# #     list_metrics += [extract_metrics_list]

# # print(list_comments, list_metrics)
    
=======
comment_dict = {}
for i in videos_list:
    comments_dicts = get_comments(i, apiKey=api_key)['items']
    clean_comments_list = clean_comments(comments_dicts)
    dict_comments = {
        "videoId": i,
        "comments": clean_comments_list
    }
    list_comments += [dict_comments]
    metrics_dicts = get_metrics(i, apiKey=api_key)
    extract_metrics_list = extract_metrics(metrics_dicts)
    list_metrics += [extract_metrics_list]
    comment_dict['videoId']= list_comments
    my_big_fat_df= pd.DataFrame(comment_dict['videoId'])
print(my_big_fat_df)
>>>>>>> f81ef572f4ebb8fb025d6fb4ec75d775b7d6ef27
