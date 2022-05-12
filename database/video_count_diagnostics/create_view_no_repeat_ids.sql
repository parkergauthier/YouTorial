-- use to count number of unique videos in youtube_ids which do not have metrics
create view no_repeat_ids as
select distinct "videoID"
from unique_id
where "videoID" no in (
select disticnt "videoID"
from youtube_metrics)