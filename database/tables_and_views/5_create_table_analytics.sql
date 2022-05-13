-- use to store video data with analyzed text data scores 
create table analytics as(
videoID varchar,
views_count numeric,
likes numeric,
comments_ numeric,
length_ interval,
like_ratio numeric,
comment_ratio numeric,
polarity numeric,
subjectivity numeric)