# %%
import os
import googleapiclient.discovery
import pandas as pd
import json

from sqlalchemy import values
from metrics import get_metrics, extract_metrics
from random import sample
from comments_request import get_comments, clean_comments


# Setting Paths
API_BASE_DIR = "/Users/amalkadri/Documents/GitHub/YouTorial/scraping"
API_KEY_PATH = os.path.join(API_BASE_DIR, "api_keyPG.txt")
JSON_PATH_IN = os.path.join(API_BASE_DIR, "500_videos.json")

# Reading API Key
# with open(API_KEY_PATH) as f:
#     api_key = f.readline()
api_key = 'AIzaSyAtZPilsatG7GcuEKKB1fX-mLSpwsIkydQ'
#Reading in JSON
with open(JSON_PATH_IN, "r") as f:
    videos = json.load(f)

videos_list = ["SwSbnmqk3zY", videos['videoID']['1'],
               videos['videoID']['2'], videos['videoID']['3'], videos['videoID']['4']]

# videos_list
# videos_ex = sample(videos["VideoID"],2) # Replace this later

# %%
list_comments = []
list_metrics = []

for i in videos_list:
    comments_dicts = get_comments(i)['items']
    clean_comments_list = clean_comments(comments_dicts)
    dict_comments = {
        "videoId": i,
        "comments": clean_comments_list
    }
    # if i not in list_comments["videoId"]:
    list_comments += [dict_comments]

    metrics_dicts = get_metrics(i)
    print(metrics_dicts)
    extract_metrics_list = extract_metrics(metrics_dicts)

    # if i not in list_metrics["videoId"]:
    list_metrics += [extract_metrics_list]

print(list_comments, list_metrics)

# %%
