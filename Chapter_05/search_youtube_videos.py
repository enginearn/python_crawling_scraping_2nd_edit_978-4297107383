#!/usr/bin/env python3

# curl
# curl "https://www.googleapis.com/youtube/v3/search?key=$API_KEY&part=snippet&q=hololive&type=video"
# curl "https://www.googleapis.com/youtube/v3/videos?key=$API_KEY&part=snippet&id=_DeqC97LOLg&part=snippet,statistics"

import os
import sys

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv(".env")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

api_service_name = "youtube"
api_version = "v3"

youtube = build(api_service_name, api_version, developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part="snippet",
    q="rust",
    type="video",
).execute()

for item in search_response["items"]:
    print(item["snippet"]["title"])

if __name__ == '__main__':
    sys.exit(0)

