#!/usr/bin/env python
# MagicConchBot/bots/magic-conch-bot.py

import tweepy
import logging
import time
import os
import random
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def pick_response():
    responses = ["no.", "try asking again.", "nOoOoo.",
                 "Maybe someday.", "I don't think so.", "yes."]
    length = len(responses)
    random_number = random.randint(0, length)
    response = responses[random_number]
    logger.info(response)
    return response


def check_mentions(api, since_id):
    if type(since_id) is not int:
        since_id = int(since_id)
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        key = "?"
        if any(keyword in tweet.text.lower() for keyword in key):
            logger.info(f"Answering to {tweet.user.name}")
            logger.info(tweet.id)

            status = pick_response()
            api.update_status(
                status=status,
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )

    f = open("lastTweet.txt", "w")
    new_since_id = str(new_since_id)
    f.write(new_since_id)
    f.close()

    return new_since_id


def main():
    api = create_api()
    f = open("lastTweet.txt", "r")
    lastTweet = int(f.readline())
    f.close()
    since_id = lastTweet
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(10)


if __name__ == "__main__":
    main()
