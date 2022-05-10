# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import googleapiclient.discovery
import json

# from metrics_karlo import API_KEY

BASE_DIR = "scraping"
KEY_PATH = os.path.join(BASE_DIR, "api_keys.json")

with open(KEY_PATH, "r") as f:
    api_key_dict = json.load(f)
api_key = api_key_dict["Amal_key"]


def get_metrics(video_id, apiKey=api_key):
    """Retrieves a dictionary from the YouTube Data API for information on views, likes, and comment counts."""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = apiKey

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.videos().list(part="statistics, contentDetails", id=video_id)
    response = request.execute()

    return response


def extract_metrics(metrics_dict):

    clean_dict = {
        "videoID": metrics_dict["items"][0]["id"],
        "likes": metrics_dict["items"][0]["statistics"]["likeCount"],
        "comments": metrics_dict["items"][0]["statistics"]["commentCount"],
        "length": metrics_dict["items"][0]["contentDetails"]["duration"],
        "views": metrics_dict["items"][0]["statistics"]["viewCount"],
    }

    return clean_dict


if __name__ == "__main__":
    print(extract_metrics(get_metrics("pb4xXXEA8zk")))
