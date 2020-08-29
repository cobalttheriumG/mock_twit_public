import tweepy
import re
from bot_tools import write_last_seen_id, get_last_seen_id, mock_tweet

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
FILE_TXT = 'last_seen_id.txt'


def mocking():
    regex = r"pl[aei]{0,2}s[ei]"
    print('Retrieving tweet...')
    since_id = get_last_seen_id(FILE_TXT)
    mentions = api.mentions_timeline(since_id, tweet_mode='extended')
    for mention in mentions:
        if re.search(regex, mention.full_text):
            mock_type = re.search(regex, mention.full_text).group()
            last_seen_id = mention.id_str
            in_reply_id = mention.in_reply_to_status_id_str
            get_mock_tweet = get_status_in_reply_txt(in_reply_id)
            tweet = mock_tweet(get_mock_tweet, mock_type)
            post_reply(tweet, 'upload.jpg', mention.id)
            write_last_seen_id(last_seen_id, FILE_TXT)


def get_status_in_reply_txt(in_reply_id):
    regex = r"https://[a-zA-Z0-9./]+"
    status_in_reply = api.get_status(in_reply_id, tweet_mode='extended')
    tweet = status_in_reply.full_text
    fix_tweet_txt = re.sub(regex, '', tweet)
    return fix_tweet_txt


def post_reply(twt, img, mention_id):
    api.update_with_media(
        img, f'{twt}', in_reply_to_status_id=mention_id, auto_populate_reply_metadata=True)
    print('tweet has replied!')
