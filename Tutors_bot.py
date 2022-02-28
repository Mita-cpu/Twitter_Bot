# import packages
import pip
import tweepy
import time


#Authenticate to Twitter
consumer_key='tqrYTWJRIuF73NhagjdTP2m4f'
consumer_secret='sKV9eR1OGyA4R4Bi0Znn9i3Coo36m3G9ggXwkGo7yEwdhnxOlx'
access_key ='1418253950751494149-8FYrY4w80UbmpQsx76PKnxkcGHjwhs'
acess_secret='NnML9HvHSAhkksBCTazZm4Nta6NBszXIO2LJRuPUJtDy2'


#Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


user = api.verify_credentials()
search_tweets = "Calculus"
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search_tweets,search_tweets).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        
    except tweepy.errors.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break