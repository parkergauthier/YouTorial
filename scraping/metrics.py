import os
import googleapiclient.discovery
import json

BASE_DIR = "scraping"
KEY_PATH = os.path.join(BASE_DIR, "file_dependencies/your_api_keys.json")

# Reading API Key
with open(KEY_PATH, "r") as f:
    api_keys = json.load(f)
api_key = api_keys["Key1"]


def get_metrics(video_id, apiKey):
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
    try:
        request = youtube.videos().list(part="statistics, contentDetails", id=video_id)
        response = request.execute()
    except googleapiclient.errors.HttpError as API_ERROR:
        print(
            "==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*"
        )
        print(API_ERROR)
        print(
            "ERROR: [Metrics] Request could not be processed. Check to see if your API key has met it's quota"
        )
        print(
            "==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*"
        )
        quit()

    return response


def extract_metrics(metrics_dict):
    """Takes information from a dictionary associated with a video and collects metrics of interest"""
    if metrics_dict["items"] == []:
        print("This video has no metrics, it may have been deleted")
        pass

    clean_dict = {
        "videoID": metrics_dict["items"][0]["id"],
    }

    try:
        clean_dict["likes"] = metrics_dict["items"][0]["statistics"]["likeCount"]
    except:
        clean_dict["likes"] = -1

    try:
        clean_dict["comments"] = metrics_dict["items"][0]["statistics"]["commentCount"]
    except:
        clean_dict["comments"] = -1

    try:
        clean_dict["length"] = metrics_dict["items"][0]["contentDetails"]["duration"]
    except:
        clean_dict["length"] = -1

    try:
        clean_dict["views"] = metrics_dict["items"][0]["statistics"]["viewCount"]
    except:
        clean_dict["view"] = -1

    return clean_dict


if __name__ == "__main__":
    # print(extract_metrics(get_metrics("hQkJOP7CBII")))
    # print(get_metrics("x2XTxT38jms"))
    print((get_metrics("9Zxwm3b6Dy4", apiKey=api_key)))
