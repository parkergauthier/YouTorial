#%%
# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# map used to plot circles:
# https://www.mapdevelopers.com/draw-circle-tool.php?circles=%5B%5B1000000%2C31.8986083%2C-103.3465565%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%2C%5B1000000%2C41.5647182%2C-116.3364002%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%2C%5B1000000%2C33.4940108%2C-84.3442127%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%2C%5B1000000%2C46.0955066%2C-94.5818799%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%2C%5B1000000%2C44.9253219%2C-71.7303174%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%5D

import os
import googleapiclient.discovery
import pandas as pd
import json

# BASE_DIR = "../scraping"
# KEY_PATH = os.path.join(BASE_DIR, "api_keyPG.txt")

# with open(KEY_PATH) as f:
#     api_key = f.readline()

#%%
def request_search_results(token="", region_center="31.898608,-103.346556"):
    """requests 50 search results for a specified query using the Youtube Data API V3, returns a complex dictionary"""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "REDACTED"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            topicId="/m/032tl | /m/01k8wb | /m/027x7n | /m/02wbm",
            pageToken=token,
            q="how to | tutorial | recipe | step | lesson | guide | demo | DIY",
            type="video",
            videoCategoryId="26",
            regionCode="US",
            location=region_center,
            locationRadius="1000km",
        )
        response = request.execute()
    except NameError:
        print("OOPS")
    except IOError:
        print("error arises bc file can’t be opened")
    except KeyboardInterrupt:
        print("error arises when an unrequired key is pressed by the user")
    except ValueError:
        print("error arises when built-in function receives a wrong argument")
    except EOFError:
        print("error arises bc End-Of-File is hit without reading any data")
    except ImportError:
        print("error arises bc it is unable to find the module")
    else:
        return response
