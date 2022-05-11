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

# Global Variables
conn_string = "postgresql://youtube-project:Zhanghaokun_6@35.226.197.36/youtube-content"
engine = sqlalchemy.create_engine(conn_string)

sql_data = pd.read_sql_table('youtube_metrics', engine)

stop_words = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

# Functions:


def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('/(\s\s\s*)/g', ' ', text)
    return text


def get_sentiment(txt):
    doc = nlp(txt)
    sentiment_list = [doc._.blob.polarity, doc._.blob.subjectivity]
    return sentiment_list


sentiment_getter = get_sentiment

####################
if __name__ == "__main__":
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

    ID_to_send_to_sql_comments = metrics['videoID']
    # have to get the comments first, adjust this
    comments_df = pd.read_sql_table('youtube_comments', engine)

    one_id = comments_df[comments_df['videoID'] ==
                         'SwSbnmqk3zY']  # not necessary in production
    comment_list = one_id['comment'].to_list()
    dirty_text = ' '.join(comment_list)
    clean = clean_text(dirty_text)
    sentiment = get_sentiment(clean)

    analysis['polarity'] = sentiment[0]
    analysis['subjectivity'] = sentiment[1]
    analysis
