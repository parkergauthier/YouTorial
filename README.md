# YouTorial

## Goal

## Methodology

### API Scraping

The first component of this project entailed scraping YouTube's V3 API. Specifically, we utilized YouTube's API explorer as a starting point for our own scripts to acquire desired video data: metrics and comments. To do this, we needed to start at a search result. A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data. Thus, after this we turned to the videos end point to gather the necessary, aforementioned data. The search results were specified so we query only "How To" category videos on Youtube throughout the 5 U.S. regions as specified by YouTube's regional parameters. Once one script was able to query the searches, then the others gathered the data from videos. We then looped the former and latter instances to reflect a complete product of data for each video to use for analyis. These features included: video title, video length, number of views, number of likes, number of comments, and the comments themselves. The comments are a crucial component to our analysis as will be discussed in further detaili in the 'Analysis' section of this README.md.

### Database Management

Our workflow for database management was as follows. Once we scraped YouTube's API, we honed in on unique video ID's to populate one table of the Video ID, Video Title, and Channel ID. Using a python script, we queried a distinct list of Video ID's and fed the list into a function which extracted metrics and comments. The function then sent these two separate groups of data to populate two separate tables since they have fundamentally different structures. This process was implemented for tens of thousands of videos. The main task for this team was to iteratvely populate our database while organizing the data structures.

### Analysis and Findings

### GUI 
To build our web app that shows user the top six recommended tutorials based on our sentiment analysis and ranking algorithm, we used Streamlit, a free online Python-based tool. We first used SQLAlchemy to connect to our GCP-hosted database and query the top six video ID's based on the user's search entry. We then pasted these id's with the base YouTube url to create a list of links to the recommended videos. From there, we used an extraneous package called streamlit_player to directly loop through this list and embed the selected videos onto our web app. After some creative layout-wrangling, we deployed the web app using Streamlit through our Github repository for public use.  

## Instructions for reproduction


## Future Work 
While we have a fully operational algorithm to recommend the right videos based on a user's search, our final product suffers from a lack of data. Due to query constraints in scraping videos using the YouTube API, we were limited to how large of a database we can feasibly build within the timeframe of this project. In the future, building out a library of API keys through GCP would allow us to automatically populate our database to provide better recommendations to users. 
