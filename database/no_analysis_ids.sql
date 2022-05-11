CREATE view no_analysis AS 
SELECT DISTINCT "videoID"
FROM youtube_metrics
WHERE "videoID" NOT IN
(SELECT distinct"videoID"
FROM analytics);