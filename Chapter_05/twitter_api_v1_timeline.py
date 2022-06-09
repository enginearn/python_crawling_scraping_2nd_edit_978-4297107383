import os
import json
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv

load_dotenv(".env")

TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_KEY_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

twitter = OAuth1Session(TWITTER_API_KEY,
                        client_secret = TWITTER_API_KEY_SECRET,
                        resource_owner_key = TWITTER_ACCESS_TOKEN,
                        resource_owner_secret = TWITTER_ACCESS_TOKEN_SECRET)

response = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json")
print(json.dumps(response.json()["errors"][0]["message"]))
for status in response.json():
    print(f"status: {status}")
    print(f"@{status['user']['screen_name']}, {status['text']}")
