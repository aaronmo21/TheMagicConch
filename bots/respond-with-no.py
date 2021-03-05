#!/usr/bin/env python
#RespondsWithNo/bots/respond-with-no.py

import tweepy
import logging
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_api():
    consumer_key = "EuikJ7SURGxvAgqVnqbMe7lp6"
    consumer_secret = "8fvhb5cBL0KJ3qNqwEX5P8s4YKAL0xlLiq8eBooiWy8tePJxjV"
    access_token = "1366182774139404291-FoCqyNRfFj6HzYgmutI7PNU0zWhe1M"
    access_token_secret = "yoat0ZRcnMWy4JezpLprvp2WGXmygPWNoLIqOgy0NTVgK"

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

def check_mentions(api, since_id):
    if type(since_id) is not int:
        since_id = int(since_id)
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        logger.info(f"Answering to {tweet.user.name}")
        logger.info(tweet.id)

        api.update_status(
            status="no.",
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True
        )

    f = open("lastTweet.txt","w")
    new_since_id = str(new_since_id)
    f.write(new_since_id)
    f.close()

    return new_since_id

def main():
    api = create_api()
    f = open("lastTweet.txt","r")
    lastTweet = int(f.readline())
    f.close()
    since_id = lastTweet
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()