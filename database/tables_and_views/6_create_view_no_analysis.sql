-- use as query table to feed videos from youtube_metrics and youtube_comments into analytics
CREATE view no_analysis AS 
SELECT *
FROM youtube_metrics
WHERE "videoID" NOT IN
(SELECT distinct"videoID"
FROM analytics);