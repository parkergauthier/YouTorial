select * from test_table_unique;

create view test_table_unique as
SELECT "videoID" 
FROM test_table
group by "videoID";