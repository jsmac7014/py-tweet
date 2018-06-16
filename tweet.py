import tweepy
import re
from collections import Counter
from konlpy.tag import Hannanum


auth = tweepy.OAuthHandler('K4NlAUWmqwVCkpamGBad8k8Ch', 'rGq7NiT3EfSwhQUhuBzjWztFFexqsoxPPqDD5yFGGbhnlLX5pG')
auth.set_access_token('1006478908055642115-cOc2iVSnOGeuxhMAIg6jocIuqqjmKo', 'QX5ewU1RpPuRAapNqIMFOnqlrbCoS8zu6liqupwVUQAeu')

api = tweepy.API(auth)

def _get_tweet(username, count):
    tweet_list = []
    for tweet in tweepy.Cursor(api.user_timeline, id=username,tweet_mode='extended').items(int(count)):
        tweet_list.append(re.sub(r"http\S+", "", tweet.full_text))
    return_list = ' '.join(tweet_list)
    return return_list

def _count(text):
    h = Hannanum()
    nouns = h.nouns(text)
    counted = Counter(nouns)
    return counted

def get_result(username, count):
    list = _get_tweet(username, count)
    result = _count(list)
    return result





