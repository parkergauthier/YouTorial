import os
import googleapiclient.discovery
import pandas as pd
import json

from sqlalchemy import values
from metrics import get_metrics, extract_metrics
from random import sample
from comments_request import get_comments, clean_comments


# Setting Paths
API_BASE_DIR = "scraping"
API_KEY_PATH = os.path.join(API_BASE_DIR, "api_keys.json")
JSON_PATH_IN = os.path.join(API_BASE_DIR, "500_videos.json")

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

for i in videos_list:
    comments_dicts = get_comments(i, apiKey=api_key)['items']
    clean_comments_list = clean_comments(comments_dicts)
    dict_comments = {
        "videoId": i,
        "comments": clean_comments_list
    }

    list_comments += [dict_comments]

    metrics_dicts = get_metrics(i, apiKey=api_key)
    print(metrics_dicts)
    extract_metrics_list = extract_metrics(metrics_dicts)

    list_metrics += [extract_metrics_list]

print(list_comments, list_metrics)
