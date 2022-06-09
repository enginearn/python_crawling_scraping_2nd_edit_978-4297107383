import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(".env")
BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")

user = "enginyaaaaan"

def get_user_id():
    usernames = f"usernames={user}"
    user_fields = "user.fields=description,created_at"
    url = f"https://api.twitter.com/2/users/by?{usernames}"

    return url

def create_url(id):
    url = f"https://api.twitter.com/2/users/{id}/tweets"

    return url

def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}

def bearer_oauth(r):
    """
    Method required by bearer token authentication
    """
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"

    return r

def connect_to_endpoint_4_user_id(url):
    response = requests.get(url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()

def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}")

    return response.json()

def main():
    url = get_user_id()
    json_response = connect_to_endpoint_4_user_id(url)
    user_id = json.dumps(json_response["data"][0]["id"]).replace('"', '')
    print(user_id)
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == "__main__":
    main()
