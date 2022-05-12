import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import json

f = open("C:/Users/Haokun Zhang/Downloads/500_videos.json")

dict_of_video_dicts = json.load(f)
f.close()

df = pd.DataFrame.from_dict(dict_of_video_dicts)

conn_string = "postgresql://youtube-project:Zhanghaokun_6@35.226.197.36/youtube-content"
db = create_engine(conn_string)
conn = db.connect()
df.to_sql(con=conn, name="test_table", if_exists="replace")
