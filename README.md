# YouTorial

## Goal
YouTube's own recommendation engine relies on a variety of factors, some metrics visible to users (likes, views, etc.), and some (personalized results, promoted/sponsored videos, viral hits, etc.) that affect the videos recommended to users. In particular, searches for 'how-to' and tutorial videos tend to return results of varying quality and relevance. Our goal for this project is build our own recommendation algorithm that uses sentiment analysis of comments, likes, views, video lengths, objectivity scores, and other key metrics. 

## Methodology

### API Scraping

The first component of this project entailed scraping YouTube's V3 API. Specifically, we utilized YouTube's API explorer as a starting point for our own scripts to acquire desired video data: metrics and comments. To do this, we needed to start with a search result. A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data. Thus, after this, we turned to the video’s endpoint to gather the necessary, aforementioned data. The search results were specified so we query only "How To" category videos on Youtube throughout the 5 U.S. regions as specified by YouTube's regional parameters. Once one script queried the searches, the others gathered the data from videos. We then looped the former and latter instances to reflect a complete product of data for each video to use for analysis. These features included: video title, video length, number of views, number of likes, number of comments, and the comments themselves. The comments are a crucial component of our analysis as will be discussed in further detail in the 'Analysis' section of this README.md.

**Stages:**

Stage 1.)

Stage 2.) In this phase, we used video IDs from Stage 1 (obtained from our SQL database) to gather comments and metrics from each video.  These were used to again query the YouTube Data API using the endpoints *commentThreads* for comments and *videos* for likes, number of comments, views, and length.  Each of these queries returned a dictionary that contained information about a requested video.   These were then cleaned using functions designed to extract the relevant information for our analysis.  Using the cleaned data, dataframes were constructed to append two tables in our database, one for comments and one for metrics.  The comments table contained a row for each individual comment and its respective video ID, while the metrics table contained one row per video with columns for its metrics.

### Database Management

Our workflow for database management was as follows. Once we scraped YouTube's API, we honed in on unique video ID's to populate one table of the Video ID, Video Title, and Channel ID. Using a python script, we queried a distinct list of Video ID's and fed the list into a function which extracted metrics and comments. The function then sent these two separate groups of data to populate two separate tables since they have fundamentally different structures. This process was implemented for tens of thousands of videos. The main task for this team was to iteratvely populate our database while organizing the data structures.

### Analysis and Findings

### GUI 
To build our web app that shows user the top six recommended tutorials based on our sentiment analysis and ranking algorithm, we used Streamlit, a free online Python-based tool. We first used SQLAlchemy to connect to our GCP-hosted database and query the top six video ID's based on the user's search entry. We then pasted these id's with the base YouTube url to create a list of links to the recommended videos. From there, we used an extraneous package called streamlit_player to directly loop through this list and embed the selected videos onto our web app. After some creative layout-wrangling, we deployed the web app using Streamlit through our Github repository for public use. 

![salsa-demo](https://user-images.githubusercontent.com/98052656/168164904-cde501ad-1696-4e29-9e12-84d327171c5e.gif)

## Instructions for reproduction


## Future Work 
While we have a fully operational algorithm to recommend the right videos based on a user's search, our final product suffers from a lack of data. Due to query constraints in scraping videos using the YouTube API, we were limited to how large of a database we can feasibly build within the timeframe of this project. In the future, building out a library of API keys through GCP would allow us to automatically populate our database to provide better recommendations to users. In addition, access to dislike metrics and the ability to perform word association analysis would vastly improve our algorithm. 
