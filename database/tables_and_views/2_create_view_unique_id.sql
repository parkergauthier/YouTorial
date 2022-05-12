-- use to filter duplicate videos from youtube_id for subsequent views
-- use count function to count total number of unique videos
create view unique_id as
select distinct("videoID")
from youtube_id