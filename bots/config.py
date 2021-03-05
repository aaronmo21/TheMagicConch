# RespondsWithNo/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("EuikJ7SURGxvAgqVnqbMe7lp6")
    consumer_secret = os.getenv("8fvhb5cBL0KJ3qNqwEX5P8s4YKAL0xlLiq8eBooiWy8tePJxjV")
    access_token = os.getenv("1366182774139404291-FoCqyNRfFj6HzYgmutI7PNU0zWhe1M")
    access_token_secret = os.getenv("yoat0ZRcnMWy4JezpLprvp2WGXmygPWNoLIqOgy0NTVgK")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api