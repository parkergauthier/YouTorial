# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery


def get_comments():
    """Retrieves a dictionary from the YouTube Data API for information on comment threads."""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "API KEY!! Ask Parker if you need help"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet,replies", videoId="QuGCXXeJV5Y"
    )
    response = request.execute()

    return response


def clean_comments(comments):
    """Extracts comments from comments-threads dictionary and saves comments into a list of strings"""
    comment_list = []

    for i in range(19):
        comment_list += [
            comments["items"][i]["snippet"]["topLevelComment"]["snippet"][
                "textOriginal"
            ]
        ]

    return print(comment_list)


if __name__ == "__main__":
    clean_comments(get_comments())
