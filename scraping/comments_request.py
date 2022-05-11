import os
import googleapiclient.discovery
import json

BASE_DIR = "scraping"
KEY_PATH = os.path.join(BASE_DIR, "api_keys.json")

# with open(KEY_PATH) as f:
# api_key = f.readline()
with open(KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys["Parker_key"]

sample_id = "pb4xXXEA8zk"  # change with variable later, just to make the code run


def get_comments(video_id, apiKey=api_key):
    """Uses the youtube v3 API to get the commentsThread:list object with 25 comments"""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = apiKey

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )
    try:
        request = youtube.commentThreads().list(
            part="snippet", maxResults=25, order="relevance", pageToken="", videoId=video_id
        )
        response = request.execute()
    except googleapiclient.errors.HttpError as API_ERROR:
        print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*")
        print(API_ERROR)
        print(
            "ERROR: [Comments] Request could not be processed. Check to see if your API key has met it's quota")
        print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*")
        quit()

    return response


def clean_comments(comments_dict):
    """Extracts comments from comments-threads dictionary and saves comments into a list of strings"""
    comment_list = []

    for i in range(comments_dict["pageInfo"]["totalResults"]):
        comment_list += [
            comments_dict["items"][i]["snippet"]["topLevelComment"]["snippet"][
                "textOriginal"
            ]
        ]

    return comment_list


if __name__ == "__main__":
    # print(clean_comments(get_comments("1vmLVzU4KD8")))
    print(get_comments("1vmLVzU4KD8"))
