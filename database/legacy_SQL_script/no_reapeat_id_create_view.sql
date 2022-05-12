create view no_repeat_ids as
select "videoID" 
from unique_id
where "videoID" not in 
(select "videoID"  
from youtube_metrics yc)