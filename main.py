from mock_bot import mocking
import tweepy
import time

if __name__ == '__main__':
    while True:
        try:
            mocking()
            time.sleep(15)
        except tweepy.RateLimitError as err:
            print(f'Error : {err}')
