import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import json

f = open("")

dict_of_video_dicts = json.load(f)
f.close()

df = pd.DataFrame.from_dict(dict_of_video_dicts)

conn_string = ""
db = create_engine(conn_string)
conn = db.connect()
df.to_sql(con=conn, name="", if_exists="replace")
