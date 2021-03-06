# Currently encounters runtime
# loading packages
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
from database import conn_query
py.init_notebook_mode(connected=True)
import wordcloud
from collections import Counter


# connect to the database

curs = conn_query.cursor()

# the SQL code which select data from the table
sql_a = 'select * from analytics'

# execute the SQL code in database
curs.execute(sql_a)

# obtain the data
data_analytics = curs.fetchall()

# close
curs.close()

# data_analytics.columns =list('')
data_analytics = pd.DataFrame(data_analytics, columns=['videoID', 'views_count', 'likes',
                                                       'comments_', 'length_', 'like_ratios', 'comment_ratio', 'polarity', 'subjectivity'])
# df = pd.DataFrame(my_list, columns = ['Names'])
print(data_analytics)


# Videos views according to their Likes and Comments
plt.figure(figsize=(16, 8))
plt.title('Videos views according to their Likes and Comments',
          fontsize=20, fontweight='bold', y=1.05,)
plt.xlabel('Likes', fontsize=15)
plt.ylabel('Comments', fontsize=15)

likes = data_analytics["likes"].values
comments_ = data_analytics["comments_"].values
views = data_analytics["views_count"].values
likes_ratio = data_analytics["like_ratios"].values
comment_ratio = data_analytics['comment_ratio'].values
length = data_analytics['length_'].values
polarity = data_analytics['polarity'].values
subjectivity = data_analytics['subjectivity'].values


plt.scatter(likes, comments_, s=views.astype(
    float) / 20000, edgecolors='white')
plt.show()


# normal distribution check：
data_analytics['likes_log'] = np.log(
    data_analytics['likes'].to_numpy(dtype=int) + 1)
data_analytics['views_log'] = np.log(
    data_analytics['views_count'].to_numpy(dtype=int) + 1)
data_analytics['comment_log'] = np.log(
    data_analytics['comments_'].to_numpy(dtype=int) + 1)
data_analytics.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

plt.figure(figsize=(12, 6))


# show the correlation
plt.figure(figsize=(12, 8))

# correlation analysis
sns.heatmap(data_analytics[['views_log', 'likes_log', 'comment_log',
                            'polarity', 'subjectivity']].corr(), annot=True)
plt.show()

# plt.figure(figsize=(15,10))
# ax = sns.heatmap(data_analytics.corr(),annot=True)
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)

# plot views-like
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['likes'],
                color='#ffa600', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Likes")
_ = ax.set_title('Views - Likes Scatter Plot')

# plot views-comments
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['comments_'],
                color='lightcoral', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Comments")
_ = ax.set_title('Views - Comments Scatter Plot')

# plot views-polarity
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['polarity'],
                color='#87CEFA', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Polarity")
_ = ax.set_title('Views - Polarity Scatter Plot')

# plot views-subjectivity
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['subjectivity'],
                color='#B0C4DE', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Views", ylabel="Subjectivity")
_ = ax.set_title('Views - Subjectivity Scatter Plot')


# plot likes-comments
fig, ax = plt.subplots()
_ = plt.scatter(x=data_analytics['likes'], y=data_analytics['comments_'],
                color='tomato', edgecolors="#000000", linewidths=0.5)
_ = ax.set(xlabel="Likes", ylabel="Comments")
_ = ax.set_title('Likes - Comments Scatter Plot')

# # plot length - likes
# fig, ax = plt.subplots()
# _ = plt.scatter(x=data_analytics['views_count'], y=data_analytics['length_'], color='#000080', edgecolors="#000000", linewidths=0.5)
# _ = ax.set(xlabel="Views", ylabel="Length")
# _ = ax.set_title('Views - Length Scatter Plot')


# views log distribution
plt.show()
g1 = sns.distplot(data_analytics['views_log'])
g1.set_title("VIEWS LOG DISTRIBUTION", fontsize=16)

plt.show()
g2 = sns.distplot(data_analytics['likes_log'])
g2.set_title("LIKES LOG DISTRIBUTION", fontsize=16)

plt.show()
g3 = sns.distplot(data_analytics['comment_log'])
g3.set_title("COMMENTS LOG DISTRIBUTION", fontsize=16)

plt.show()
g4 = sns.distplot(data_analytics['polarity'])
g4.set_title("POLARITY DISTRIBUTION", fontsize=16)

plt.show()
g5 = sns.distplot(data_analytics['subjectivity'])
g5.set_title("SUBJECTIVITY DISTRIBUITION", fontsize=16)


# connect to the database

curs = conn_query.cursor()

# the SQL code which select data from the table
sql_a = 'select * from youtube_comments'

# execute the SQL code in database
curs.execute(sql_a)

# obtain the data
youtubecmnts = curs.fetchall()

# close
curs.close()

# data_analytics.columns =list('')
youtubecmnts = pd.DataFrame(youtubecmnts, columns=[
                            'index', 'VideoID', 'comment'])
# df = pd.DataFrame(my_list, columns = ['Names'])
print(youtubecmnts)

# wordcloud
plt.figure(figsize=(15, 15))

cmntslist = list(youtubecmnts['comment'].apply(lambda x: x.split()))
cmntslist = [x for y in cmntslist for x in y]
# top30words = Counter(cmntslist).most_common(30)
# cmnts = pd.DataFrame(top30words, columns=['words','frequency'])
# print(cmnts)
wc = Counter(cmntslist).most_common(30)
#  print(wc)
# cmnts = pd.DataFrame(wc, columns=['words','frequency'])
# print(cmnts)

wc = wordcloud.WordCloud(width=1200, height=500, 
                         collocations=False, background_color="white", 
                         colormap="tab20b").generate(" ".join(cmntslist))
plt.figure(figsize=(15,10))
plt.imshow(wc, interpolation='bilinear')
_ = plt.axis("off")
