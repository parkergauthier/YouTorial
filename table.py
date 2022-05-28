import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

dict_of_video_dicts = {
    "Lb8IvzIeEaA": {
        "videoID": "Lb8IvzIeEaA",
        "title": "How to make a Perfectly juicy SHEPHERD’S PIE | Cottage Pie Recipe | Mansa Queen",
    },
    "0sBsoMjbdXU": {
        "videoID": "0sBsoMjbdXU",
        "title": "How To Make Walls, Roofs, Stairs For Chicken Coops - New Life [Ep 56]",
    },
}

df = pd.DataFrame.from_dict(dict_of_video_dicts, orient="index")

conn_string = #'redacted'
db = create_engine(conn_string)
conn = db.connect()
df.to_sql(con=conn, name='test_table', if_exists='replace')

