from textwrap import indent
from urllib import response
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(".env")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

user = "enginyaaaaan"

def get_user_id():
    usernames = f"usernames={user}"
    user_fields = "user.fields=description,created_at"
    url_for_user_id = f"https://api.twitter.com/2/users/by?{usernames}"
    return url_for_user_id

def create_url(id):
    url = f"https://api.twitter.com/2/users/{id}/tweets"

    return url

def bear_oauth(r):
    """
    Method required by bearer token authentication
    """
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"

    return r

def connect_to_endpoint(url):
    response = requests.get(url, auth=bear_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()

def main():
    url = get_user_id()
    json_response = connect_to_endpoint(url)
    user_id = json.dumps(json_response["data"][0]["id"])
    url = create_url(user_id)
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main":
    main()
