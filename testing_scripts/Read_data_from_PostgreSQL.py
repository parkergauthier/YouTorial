# read data from PostgreSQL

import psycopg2
import pandas as pd

# connect to the database
conn = psycopg2.connect(
    database="redacted",
    user="redacted",
    password="redacted",
    host="redacted",
    port="redacted",
)

curs = conn.cursor()

# the SQL code which select data from the table
sql = "select * from youtube_metrics"

# execute the SQL code in database
curs.execute(sql)


# obtain the data
data_metrics = curs.fetchall()

# close
curs.close()

pd.DataFrame(data_metrics)
print(data_metrics)
