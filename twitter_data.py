'''
This file is not being used as the data can not be pulled from Twitter on a free developer account.
'''

import tweepy
from tweepy import OAuthHandler 

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'JIAsLLjjKvch8IN6TwFwph1zd'
        consumer_secret = 'FHf2WSRCHzucD8XTnriYvMlVrizmHImMV0NSzrJGTzy9NkLa8C'
        access_token = '1759026535418228736-MlXeVhOOhh2WgzOM04uQItZdEM4zim'
        access_token_secret = 'IW5wWKf32m6ZLZSqPRq3ji8lwmeZc0ssaNjWNveURXrHW'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
            
    
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search_tweets(q = query, count = count)
            
            
            
        except tweepy.TweepyException as e:
            # print error (if any)
            print("Error : " + str(e))
            
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = 'Donald Trump', count = 50)
    print(tweets)
        
if __name__ == "__main__":
    # calling main function
    main()