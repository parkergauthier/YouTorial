from nltk.corpus import stopwords
import pandas as pd
import sqlalchemy
import ssl
import spacy
import nltk.corpus
from sklearn.feature_extraction.text import CountVectorizer
import re
import string

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')

conn_string = "postgresql://youtube-project:Zhanghaokun_6@35.226.197.36/youtube-content"
engine = sqlalchemy.create_engine(conn_string)

sql_data = pd.read_sql_table('youtube_metrics', engine)
stop_words = stopwords.words('english')

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")


####################
metrics = sql_data.iloc[0].to_dict()  # <-- sql data
analysis = {
    'videoID': metrics['videoID'],
    'views_count': int(metrics['views']),
    'likes': int(metrics['likes']),
    'comments_': int(metrics['comments']),
    'length_': metrics['length'],
    'like_ratios': int(metrics['likes'])/int(metrics['views']),
    'comment_ratio': int(metrics['comments'])/int(metrics['views'])
}
analysis

# have to get the comments first, adjust this
comments_df = pd.read_sql_table('youtube_comments', engine)
