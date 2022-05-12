-- use to filter duplicate videos from youtube_id for subsequent views
create view unique_id as
select distinct("videoID")
from youtube_id