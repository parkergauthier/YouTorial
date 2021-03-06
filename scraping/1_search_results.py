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
from database import engine

BASE_DIR = "scraping"
KEY_PATH = os.path.join(BASE_DIR, "file_dependencies/your_api_keys.json")
TOKEN_PATH = os.path.join(BASE_DIR, "file_dependencies/tokens_file.json")

with open(KEY_PATH) as f:
    all_keys = json.load(f)
    api_key = all_keys["Key1"]


def request_search_results(query, token="", region_center="31.898608,-103.346556"):
    """requests 50 search results for a specified query using the Youtube Data API V3, returns a complex dictionary"""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            topicId="/m/032tl | /m/01k8wb | /m/027x7n | /m/02wbm",
            pageToken=token,
            q=query,
            type="video",
            order="viewCount",
            videoCategoryId="26",
            regionCode="US",
            location=region_center,
            locationRadius="1000km",
        )
        response = request.execute()
    except googleapiclient.errors.HttpError as API_ERROR:
        print(
            "==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*"
        )
        print(API_ERROR)
        print(
            "ERROR: Request could not be processed. Check to see if your API key has met it's quota"
        )
        print(
            "==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*"
        )
        quit()

    return response


def get_vid_ids(dict_list):

    id_list = []

    for i in range(len(dict_list)):
        vid_info = {
            "videoID": dict_list[i]["id"]["videoId"],
            "title": dict_list[i]["snippet"]["title"],
            "channelID": dict_list[i]["snippet"]["channelId"],
        }
        id_list.append(vid_info)
    return id_list


def get_tutorial_url_list(query, loop_len=50, track=True):
    """Calls functions to request youtube search results as a list of video IDs and titles as a dictionary, with 50 IDs per iteration"""
    full_id_list = []

    # define region centers:
    west = "41.564718,-116.336400"
    texas = "31.898608,-103.346556"
    midwest = "46.095507,-94.581880"
    southeast = "33.494011,-84.344213"
    northeast = "44.925322,-71.730317"

    print("Number of results so far:")

    for i in range(loop_len):
        with open(TOKEN_PATH, "r") as json_file:
            token_dict = json.load(json_file)

        west_soup = request_search_results(
            query, token=token_dict["west_page"], region_center=west
        )
        west_list = west_soup["items"]

        texas_soup = request_search_results(
            query, token=token_dict["texas_page"], region_center=texas
        )
        texas_list = texas_soup["items"]

        midwest_soup = request_search_results(
            query, token=token_dict["midwest_page"], region_center=midwest
        )
        midwest_list = midwest_soup["items"]

        southeast_soup = request_search_results(
            query, token=token_dict["southeast_page"], region_center=southeast
        )
        southeast_list = southeast_soup["items"]

        northeast_soup = request_search_results(
            query, token=token_dict["northeast_page"], region_center=northeast
        )
        northeast_list = northeast_soup["items"]

        full_id_list += get_vid_ids(west_list)
        full_id_list += get_vid_ids(texas_list)
        full_id_list += get_vid_ids(midwest_list)
        full_id_list += get_vid_ids(southeast_list)
        full_id_list += get_vid_ids(northeast_list)

        # transform list to dataframe

        df = pd.DataFrame(full_id_list).drop_duplicates().set_index(["videoID"])
        # print(df.shape)

        # upload dataframe to table
        df.to_sql(con=engine, name="youtube_id", if_exists="append")

        print("=========================================")
        num_results = i * 250 + 250
        if track:
            print(f"{num_results} so far!")
        # redefine tokens dict
        try:
            token_dict["west_page"] = west_soup["nextPageToken"]
            token_dict["texas_page"] = texas_soup["nextPageToken"]
            token_dict["midwest_page"] = midwest_soup["nextPageToken"]
            token_dict["southeast_page"] = southeast_soup["nextPageToken"]
            token_dict["northeast_page"] = northeast_soup["nextPageToken"]
            print(token_dict)
        except:
            token_dict = {
                "west_page": "",
                "texas_page": "",
                "midwest_page": "",
                "southeast_page": "",
                "northeast_page": "",
            }
            with open(TOKEN_PATH, "w+") as json_file:
                json.dump(token_dict, json_file)
            print("You have reached the end of Search Results for this Query :D")
            break

        with open("scraping/file_dependencies/tokens_file.json", "w+") as json_file:
            json.dump(token_dict, json_file)

    return full_id_list


if __name__ == "__main__":
    num_iterations = 1
    query = "Teach & Python | C++"
    full_vid_list = get_tutorial_url_list(query, num_iterations, track=True)
