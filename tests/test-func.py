import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("EuikJ7SURGxvAgqVnqbMe7lp6", 
    "8fvhb5cBL0KJ3qNqwEX5P8s4YKAL0xlLiq8eBooiWy8tePJxjV")
auth.set_access_token("1366182774139404291-FoCqyNRfFj6HzYgmutI7PNU0zWhe1M", 
    "yoat0ZRcnMWy4JezpLprvp2WGXmygPWNoLIqOgy0NTVgK")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#Create tweet
#api.update_status("Test tweet from Tweepy Python")

#Get user details
#user = api.get_user("aaronmomoney")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

#Update bio
#api.update_profile(description="Mention me, see what happens.")

#Like own tweet
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)