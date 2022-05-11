from nltk.corpus import stopwords
import pandas as pd
import sqlalchemy
import ssl
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import nltk.corpus
from sklearn.feature_extraction.text import CountVectorizer
import re
import string
import psycopg2
from apscheduler.schedulers.blocking import BlockingScheduler


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

#sql_data = pd.read_sql_table('youtube_metrics', engine)

stop_words = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

conn_query = psycopg2.connect(
    dbname="youtube-content",
    user="youtube-project",
    host="35.226.197.36",
    password="Zhanghaokun_6",
)
cur = conn_query.cursor()
# Functions:
# def analysis_processing(videos_num=100):


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


def sql_comments(videoID):
    """gets comments from comments database"""
    sql_comm = pd.read_sql(
        f"""select * from youtube_comments where "videoID" = '{videoID}'""", engine).drop_duplicates()
    return sql_comm


def process_comments(df):
    comment_list = df['comment'].to_list()
    dirty_text = ' '.join(comment_list)
    clean = clean_text(dirty_text)
    sentiment = get_sentiment(clean)
    return sentiment


def scheduled_upload():
    #num_database_items = 5

    #cur.execute(f"select * from no_analysis limit {num_database_items}")
    cur.execute(f"select * from no_analysis")
    i = 0
    for video in cur:
        i += 1

        metrics_tup = video
        analysis = {
            'videoID': metrics_tup[1],
            'views_count': int(metrics_tup[5]),
            'likes': int(metrics_tup[2]),
            'comments_': int(metrics_tup[3]),
            'length_': metrics_tup[4],
        }
        try:
            analysis['like_ratios'] = int(metrics_tup[2])/int(metrics_tup[5])
            analysis['comment_ratio'] = int(metrics_tup[3])/int(metrics_tup[5])
        except:
            analysis['like_ratios'] = 0
            analysis['comment_ratio'] = 0
        videodf = sql_comments(metrics_tup[1])
        sentiment = process_comments(videodf)

        analysis['polarity'] = sentiment[0]
        analysis['subjectivity'] = sentiment[1]
        sql_frame = pd.Series(analysis).to_frame().T.set_index('videoID')
        sql_frame.to_sql(con=engine, name="analytics", if_exists="append")
        print(f"{i} video uploaded successfully: {analysis['videoID']}")


####################
if __name__ == "__main__":
    # videos_num = 5

    # #cur.execute(f"select * from no_analysis limit {videos_num}")
    # cur.execute(f"select * from no_analysis")
    # i = 0
    # for video in cur:
    #     i += 1

    #     metrics_tup = video
    #     analysis = {
    #         'videoID': metrics_tup[1],
    #         'views_count': int(metrics_tup[5]),
    #         'likes': int(metrics_tup[2]),
    #         'comments_': int(metrics_tup[3]),
    #         'length_': metrics_tup[4],
    #     }
    #     try:
    #         analysis['like_ratios'] = int(metrics_tup[2])/int(metrics_tup[5])
    #         analysis['comment_ratio'] = int(metrics_tup[3])/int(metrics_tup[5])
    #     except:
    #         analysis['like_ratios'] = 0
    #         analysis['comment_ratio'] = 0
    #     videodf = sql_comments(metrics_tup[1])
    #     sentiment = process_comments(videodf)

    #     analysis['polarity'] = sentiment[0]
    #     analysis['subjectivity'] = sentiment[1]
    #     sql_frame = pd.Series(analysis).to_frame().T.set_index('videoID')
    #     sql_frame.to_sql(con=engine, name="analytics", if_exists="append")
    #     print(f"{i} video uploaded successfully: {analysis['videoID']}")
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_upload(), 'interval', hour=1)
    print("Process Scheduled! We will get results every 1 minute(s)")
    scheduler.start()
    
