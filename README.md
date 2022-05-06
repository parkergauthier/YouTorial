# YouTorial

Getting credentials:
https://developers.google.com/youtube/registering_an_application

## Web Scraping

The first component of this project entailed webscraping on YouTube's V3 API. Specifically, we utilized YouTube's API explorer as a starting point for our own scripts to acquire the desired data: metrics and comments. To do this, we needed to start at a search result. A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data. Thus, after this we turned to the videos end point to gather the necessary data. Once one script was able to query the searches, and the others to gather the data from videos, we then looped the former and latter instances to reflect a complete product of data to use in analyis. These features included: video title, video length, number of views, number of likes, number of comments, and the comments themselves. The comments are a crucial component to our analysis as will be discussed in further detaili in the 'Analysis' section of this README.md.
