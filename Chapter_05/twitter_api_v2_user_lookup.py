from urllib import response
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(".env")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

user = "enginyaaaaan"

def create_url():
    usernames = f"usernames={user},TwitterDev,TwitterAPI"
    user_fields = "user.fields=description,created_at"
    url = f"https://api.twitter.com/2/users/by?{usernames}&{user_fields}"

    return url

def bear_oauth(r):
    """
    Method required by bearer token authentication
    """
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"

    return r

def connect_to_endpoint(url):
    response = requests.get(url, auth=bear_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()

def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
