# YouTorial

## Goal
YouTube's own recommendation engine relies on a variety of factors, some metrics visible to users (likes, views, etc.), and some (personalized results, promoted/sponsored videos, viral hits, etc.) that affect the videos recommended to users. In particular, searches for 'how-to' and tutorial videos tend to return results of varying quality and relevance. Our goal for this project is build our own recommendation algorithm that uses sentiment analysis of comments, likes, views, video lengths, objectivity scores, and other key metrics. 

## Methodology

### API Requests

The first component of this project entailed scraping YouTube's V3 API. Specifically, we utilized YouTube's API explorer as a starting point for our own scripts to acquire desired video data: metrics and comments. To do this, we needed to start with a search result. A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data. Thus, after this, we turned to the video’s endpoint to gather the necessary, aforementioned data. The search results were specified so we query only "How To" category videos on Youtube throughout the 5 U.S. regions as specified by regional parameters. One script was designed to do these search queries, obtaining video IDs, titles, and channel information.  This data was then uploaded to a table in our database hosted on the Google Cloud Platform.  Next, we queried this table for uniqe video IDs using another script. This script would take the unique ID then queary YouTube's API again for features including video title, video length, number of views, number of likes, number of comments, and the comments themselves. These were uploaded to two seperate tables in our database, one for comments and one for metrics.  Finally, one script was used to query this information to consrutct the ratios of likes to views and comments to views. Additionally,  using sentiment analysis, videos were given scores between 0 and 1 for their comments' subjectivity and polarity.  Using these metrics, a Principle Componets Analysis was done to rank our videos based on a particular query.  The top six videos based on this ranking were selcted to be displayed on our GUI.

![](miscellaneous/assets/YouTorial_wordcloud.png)

### Database Management

Our workflow for database management was as follows. Once we scraped YouTube's API, we honed in on unique video ID's to populate one table of the Video ID, Video Title, and Channel ID. Using a python script, we queried a distinct list of Video ID's and fed the list into the aforementioned function which extracted metrics and comments. This process was implemented for tens of thousands of videos. The main task for this team was to iteratvely populate our database while organizing the data structures. Furthermore, diagnostic SQL views were written which selected all unique video IDs in the video ID table and included a where statement which selected only video IDs which were not in the metrics table, which allowed for quick counts of video ids without metrics or comments.  A similar "WHERE" clause was use for selecting video ids to analyze where the video id did not appear in the analytics table. Because of the volume of date analyzed making sure that videos were not double counted ensured the  efficacy of the data analysis pipeline to the final table. This view doubled as a count of videos with metrics and comments yet to be analyzed.

### Analysis and Findings

### GUI 
To build our web app that shows user the top six recommended tutorials based on our sentiment analysis and ranking algorithm, we used Streamlit, a free online Python-based tool. We first used SQLAlchemy to connect to our GCP-hosted database and query the top six video ID's based on the user's search entry. We then pasted these id's with the base YouTube url to create a list of links to the recommended videos. From there, we used an extraneous package called streamlit_player to directly loop through this list and embed the selected videos onto our web app. After some creative layout-wrangling, we deployed the web app using Streamlit through our Github repository for public use. 

![salsa-demo](https://user-images.githubusercontent.com/98052656/168164904-cde501ad-1696-4e29-9e12-84d327171c5e.gif)

## Instructions for reproduction

Step 1.) Go to Google Cloud Platform, login, go to APIs & Services/Enable APIs, enable YouTube Data API V3, then create a new API key.  Paste this to scraping/file_dependencies/demo_api_keys.json. 

Step 2.) While in GCP, go to SQL, create a new instance, go to Databases, and create a new database. Your credidentials will be on this page.  Use these to populate the .env file.

Step 3.) In DBeaver (or your SQL editor of choice), run, in order, the scripts in database/tables_and_views.  This will set up the infrustructure for the database.

Step 4.) Navigate to the scraping folder then open 1_search_results.py.  Go below the `if __name__ == "__main__":` block and specify the query you'd like to run.  Run this script.  This will populate the database with video IDs, title names, and channels associated with your query.

Step 5.) While still in the scraping folder, open 2_loop.py and run this to get the metrics and comments for the videos you obtained in Step 4.

Step 6.) Navigate to the analysis folder.  Run 3_get_analytics.py. This grabs the videos' metrics and comments from our database, does the sentiment anaylysis on the comments, calculates ratios, and then sends them back to the database.

Step 7.) Finally, in your terminal, type: python -m streamlit run gui/4_streamer.py.  This will pull up the final product.

Step 8.) Do a search for a *YouTorial* of your choice! :)

*This process is made to set up the infrustructure of this project.  Following these steps will only populate your tables with 250 videos.  You can scale this up as you see fit by changing the values in the `if __name__ == "__main__":` blocks of 1_search_results.py and 2_loop.py.  Also note that YouTube Data API V3 only allows 10,000 queries in a day.  You will need to wait until this resets to keep populating your database.*
## Conclusion
 By providing user-agnostic, unsponsored, and unpromoted results based solely on a metrics-based ranking system, YouTorial fulfills a ubiquitous market need for the recommendation of high quality tutorial videos. During our preliminary research, we realized the full extent of how the concept of virality has degraded the information landscape - many top results were short-format 'hack' videos, viral hits, or generally unhelpful results. In the context of tutorial videos, users need to quickly find high quality, instructive, and vetted tutorials, which YouTube currently fails in providing. In building our final product, one of the main takeaways we learned was how reliant YouTube's recommendation engine is on user-specific data that is tracked by Google. Our recommendation algorithm relies strictly on analyzing metrics and comments pulled from videos themselves - this does provide an unbiased and standardized recommendation, however, it also limits the strength and complexity of our ranking system. In addition, numerous limits on API keys, GCP storage, and search result querying curtailed how large we could build our database, thus impacting the quality and quantity of recommended videos returned for a user's query. Ultimately, our final product relies predominantly on the tonal analysis of comments to rank and recommend the best videos for users, providing an objective solution to a subjective problem. 
 
## Future Work 
While we have a fully operational algorithm to recommend the right videos based on a user's search, our final product suffers from a lack of data. Due to query constraints in scraping videos using the YouTube API, we were limited to how large of a database we can feasibly build within the timeframe of this project. In the future, building out a library of API keys through GCP would allow us to automatically populate our database to provide better recommendations to users. In addition, access to dislike metrics and the ability to perform word association analysis would vastly improve our algorithm. 
