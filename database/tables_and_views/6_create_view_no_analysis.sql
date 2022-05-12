-- use as query table to feed videos from youtube_metrics and youtube_comments into analytics
-- use count function to count number of videos with data yet to be analyzed
CREATE view no_analysis AS 
SELECT *
FROM youtube_metrics
WHERE "videoID" NOT IN
(SELECT distinct"videoID"
FROM analytics);