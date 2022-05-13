# import os

# import googleapiclient.discovery


# def get_vidlength():
#     """Retrieves vide length from the YouTube Data API."""
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = "AIzaSyC8HoD25F4yaK5fo-Wq06EKhC983t0-sQg"

#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, developerKey=DEVELOPER_KEY
#     )

#     request = youtube.videos().list(part="statistics", id="QuGCXXeJV5Y"
#     )
#     response = request.execute()

#     return response

# print(get_vidlength())


import re
import requests

API_KEY = ""

def request_id(id):

    url = "https://www.googleapis.com/youtube/v3/videos"

    parameters = {
        "part": "statistics,contentDetails",
        "key": API_KEY,
        "id": id
    }

    response = requests.get(url=url, params=parameters)

    return response.json()

if __name__ == "__main__":

    from pprint import pprint 
    id = ""

    pprint(request_id(id))