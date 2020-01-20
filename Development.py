import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx
from textblob import TextBlob

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

consumer_key = '4MvRITRR9qYgiZyHROEXy8zif'
consumer_secret = 'q5ZCMqiWL5kF5vklJUNR348tfQhk26Lq7AhVgbGWTATGiFDnGL'
access_token = '1131361591583281153-HMzJUAKGqFvGeS4H1xAwjzDI7DZhAB'
access_token_secret = 'vkExH4ol3lMfbUFvqTixA7tCFOHEhSU8CGsoSftCvwLwB'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)