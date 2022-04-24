import tweepy
import constants

if __name__ == '__main__':
    auth = tweepy.OAuth2AppHandler(
        constants.TWITTER_API_KEY, constants.TWITTER_SECRET_KEY
    )
    api = tweepy.API(auth)
