--select * from youtube_id full join test_table on youtube_id."videoID" = test_table."videoID" 
drop view complete_videos 

create view complete_videos as
select 
	distinct "videoID",CAST(title AS text),"channelID"
from
	(
(
	select 
		*
	from
		youtube_id
		where youtube_id."videoID" in (select distinct "videoID" from youtube_id))
union
	(
select
	distinct 
		"videoID" ,
		title ,
		"channelID"
from
		test_table
		where test_table."videoID" not in (select distinct "videoID" from youtube_id) )
) as combined_table
