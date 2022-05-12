# loading packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import psycopg2
import plotly.offline as py
py.init_notebook_mode(connected=True)
# import plotly.graph_objs as go
# import plotly.tools as tls
# import plotly.figure_factory as ff
import seaborn as sns

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
print(data_analytics)

# show the correlation
data_analytics.corr()


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


# normal distribution check：
data_analytics['likes_log'] = np.log(data_analytics['likes'].to_numpy(dtype=int) + 1)
data_analytics['views_log'] = np.log(data_analytics['views_count'].to_numpy(dtype=int) + 1)
data_analytics['comment_log'] = np.log(data_analytics['comments_'].to_numpy(dtype=int) + 1)
data_analytics.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

plt.figure(figsize = (12,6))


# plot views-like
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['likes'], color='#ffa600', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Likes")
_ = ax.set_title('Views - Likes Scatter Plot')

# plot views-comments
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['comments_'], color='lightcoral', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Comments")
_ = ax.set_title('Views - Comments Scatter Plot')

# plot likes-comments
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['likes'], y=data_analytics['comments_'], color='tomato', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Likes", ylabel="Comments")
_ = ax.set_title('Likes - Comments Scatter Plot')

# views log distribution
plt.show()
g1 = sns.distplot(data_analytics['views_log'])
g1.set_title("VIEWS LOG DISTRIBUITION", fontsize=16)

# # polarity distribution
# plt.show()
# g2 = sns.distplot(data_analytics['polarity'].astype(int),color='green')
# g2.set_title('Polarity DISTRIBUITION', fontsize=16)


# # subjectivity dirstribution
# plt.show()
# g4 = sns.distplot(data_analytics['comment_log'])
# g4.set_title("COMMENTS LOG DISTRIBUITION", fontsize=16)

# plt.subplots_adjust(wspace = 0.2, hspace = 0.4,top = 0.9)


