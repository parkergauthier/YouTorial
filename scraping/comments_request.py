# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import os
import googleapiclient.discovery
import pandas as pd
import json

BASE_DIR = 'scraping'
KEY_PATH = os.path.join(BASE_DIR, "api_keys.json")

# with open(KEY_PATH) as f:
#api_key = f.readline()
with open(KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys['Amal_key']

sample_id = 'QuGCXXeJV5Y'  # change with variable later, just to make the code run


def get_comments(video_id, apiKey=api_key):
    '''Uses the youtube v3 API to get the commentsThread:list object with 25 comments'''
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=25,
        order="relevance",
        pageToken="",
        videoId=video_id
    )
    response = request.execute()
    return(response)


def clean_comments(comments_dict):
    """Extracts comments from comments-threads dictionary and saves comments into a list of strings"""
    comment_list = []

    for i in range(len(comments_dict)):
        comment_list += [
            comments_dict[i]['snippet']['topLevelComment']['snippet']['textOriginal']
        ]

    return comment_list


def request_comments_list(videoId):
    items = get_comments(sample_id)['items']
    clean_items = clean_comments(items)
    return clean_items


if __name__ == "__main__":
    comments_list = request_comments_list(sample_id)
    # df_items = pd.DataFrame(clean_items)
    # json_items = pd.DataFrame.to_json(items)
    print(comments_list)

    # with open('comments.json', 'w') as outfile:
    #     outfile.write(json_items)

# sample to see what the items look like, mess with this however you like, remove later
# print(items[0]['snippet']['topLevelComment']['snippet']['textOriginal'])
# print(len(clean_comments(items)))
