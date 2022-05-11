# read data from PostgreSQL

import psycopg2
import pandas as pd
# connect to the database
conn = psycopg2.connect(database = 'youtube-content',user = 'youtube-project',password = 'Zhanghaokun_6', host = '35.226.197.36', port ='5432' )

curs = conn.cursor()

# the SQL code which select data from the table
sql_a = 'select * from analytics'

# execute the SQL code in database
curs.execute(sql_a)



# obtain the data
data_analytics = curs.fetchall()

# close
curs.close()

pd.DataFrame(data_analytics)
# data_analytics.columns =list('')
data_analytics = pd.DataFrame(data_analytics, columns=['videoID','views_count','likes',
'comments_','length_','like_ratios','comment_ratio','polarity','subjectivity'])
# df = pd.DataFrame(my_list, columns = ['Names'])
print(data_analytics)        