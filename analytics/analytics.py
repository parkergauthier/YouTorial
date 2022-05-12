# loading packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import psycopg2
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.offline as py
py.init_notebook_mode(connected=True)
# import plotly.graph_objs as go
# import plotly.tools as tls
# import plotly.figure_factory as ff
# import seaborn as sns

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

# data_analytics.columns =list('')
data_analytics = pd.DataFrame(data_analytics, columns=['videoID','views_count','likes',
'comments_','length_','like_ratios','comment_ratio','polarity','subjectivity'])
# df = pd.DataFrame(my_list, columns = ['Names'])
data_analytics.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
print(data_analytics)

# Videos views according to their Likes and Comments
plt.figure(figsize=(16,8))
plt.title('Videos views according to their Likes and Comments', fontsize=20, fontweight='bold', y=1.05,)
plt.xlabel('Likes', fontsize=15)
plt.ylabel('Comments', fontsize=15)

likes = data_analytics["likes"].values
comments_ = data_analytics["comments_"].values
views = data_analytics["views_count"].values

plt.scatter(likes, comments_, s = views.astype(float) / 20000, edgecolors='white')
plt.show()


