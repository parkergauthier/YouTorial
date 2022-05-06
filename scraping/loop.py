import os
import googleapiclient.discovery
import pandas as pd
import json

from sqlalchemy import values
from metrics import get_metrics, extract_metrics
from random import sample
from comments_request import get_comments, clean_comments


#Setting Paths 
API_BASE_DIR = "/Users/karlo/Documents/GitHub/YouTorial/scraping"
API_KEY_PATH = os.path.join(API_BASE_DIR, "api_keyPG.txt")
JSON_PATH_IN = os.path.join(API_BASE_DIR, "500_videos.json")

#Reading API Key
with open(API_KEY_PATH) as f:
    api_key = f.readline()

#Reading in JSON
with open(JSON_PATH_IN) as f:
    videos = f.readline()
    videos_ex = sample(videos["VideoId"],2) # Replace this later


list_comments = []
list_metrics =[]

for i in videos_ex:
    comments_dicts = get_comments(i)
    clean_comments = clean_comments(comments_dicts)
    dict_comments = {
        "videoId": i,
        "comments": [clean_comments]
    }
    if i not in list_comments["videoId"]:
        list_comments += [dict_comments]
    
    metrics_dicts = get_metrics(i)
    extract_metrics = extract_metrics(metrics_dicts)
    
    if i not in list_metrics["videoId"]:
        list_metrics += [extract_metrics]
    
print (list_comments,list_metrics)
    

