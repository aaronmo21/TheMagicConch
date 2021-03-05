import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("EuikJ7SURGxvAgqVnqbMe7lp6", 
    "8fvhb5cBL0KJ3qNqwEX5P8s4YKAL0xlLiq8eBooiWy8tePJxjV")
auth.set_access_token("1366182774139404291-FoCqyNRfFj6HzYgmutI7PNU0zWhe1M", 
    "yoat0ZRcnMWy4JezpLprvp2WGXmygPWNoLIqOgy0NTVgK")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")