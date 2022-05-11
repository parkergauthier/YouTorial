create view total_vids as
select *
from analytics a2 
where "videoID" in
(select distinct "videoID"
from analytics a)