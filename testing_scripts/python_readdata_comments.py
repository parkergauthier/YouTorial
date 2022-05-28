# read data from PostgreSQL

import psycopg2
import pandas as pd

# connect to the database
conn = psycopg2.connect(
    database="redacted",
    user="REDACTED",
    password="REDACTED",
    host="REDACTED",
    port="REDACTED",
)

curs = conn.cursor()

# the SQL code which select data from the table
sql2 = "select * from youtube_comments"

# execute the SQL code in database
curs.execute(sql2)


# obtain the data
data_comments = curs.fetchall()

# close
curs.close()

pd.DataFrame(data_comments)
print(data_comments)
