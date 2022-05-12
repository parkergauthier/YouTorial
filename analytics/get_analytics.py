from nltk.corpus import stopwords
import pandas as pd
import ssl
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import nltk.corpus
import re
import string
from apscheduler.schedulers.blocking import BlockingScheduler
from database import engine
from database import conn_query


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')

# Define Global Variables
stop_words = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

cur = conn_query.cursor()

# Define functions
def clean_text(text):
    '''clean text of miscellaneous punctuation and characters'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('/(\s\s\s*)/g', ' ', text)
    return text


def get_sentiment(txt):
    '''Perform sentiment analysis on a string of text'''
    doc = nlp(txt)
    sentiment_list = [doc._.blob.polarity, doc._.blob.subjectivity]
    return sentiment_list


sentiment_getter = get_sentiment


def sql_comments(videoID):
    '''gets comments from comments database'''
    sql_comm = pd.read_sql(
        f"""select * from youtube_comments where "videoID" = '{videoID}'""", engine).drop_duplicates()
    return sql_comm


def process_comments(df):
    '''Take in a dataframe with comments, and convert into a list of polarity and subjectivity scores'''
    comment_list = df['comment'].to_list()
    dirty_text = ' '.join(comment_list)
    clean = clean_text(dirty_text)
    sentiment = get_sentiment(clean)
    return sentiment


def scheduled_upload():
    '''Take in metrics and comments from database and compute stats for analysis'''
    # sample code if you would like to limit the query amounts commented below
    #num_database_items = 5
    #cur.execute(f"select * from no_analysis limit {num_database_items}")
    cur.execute(f'select * from no_analysis')
    i = 0
    item_count = cur.rowcount
    print(f'There are [{item_count}] rows to upload. Starting now! <3')
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
    print(f"All done! We uploaded {i} videos this round! :D")


if __name__ == "__main__":
    scheduled_upload()
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_upload, 'interval', hours=1)
    print('Process Scheduled! We will get results every 1 hours(s)')
    scheduler.start()
