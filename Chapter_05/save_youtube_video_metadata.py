#!/usr/bin/env python3

import os
import logging
from typing import Iterator, List
import sys
from dotenv import load_dotenv

from googleapiclient.discovery import build
from pymongo import MongoClient, ReplaceOne, DESCENDING
from pymongo.collection import Collection

load_dotenv(".env")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)

DATABASE = "youtube"

def main():
    """
    main処理
    """
    # mongo_client = MongoClient("localhost", 27017)
    mongo_client = MongoClient()
    db = mongo_client.list_database_names()
    print(db)
    if DATABASE in db:
        mongo_client.drop_database(DATABASE)

    collection = mongo_client.youtube.videos

    # 動画を検索してページ単位でアイテムのリストを取得
    q = "ホロライブ"
    for items_per_page in search_videos(q):
        save_to_mongodb(collection, items_per_page)

    show_top_videos(collection)

def search_videos(query: str, max_pages: int=5) -> Iterator[List[dict]]:
    """
    引数: queryで動画を検索して、ページ単位でアイテムリストをyieldで取得する
    最大 max_pages ページまで検索する
    """
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=YOUTUBE_API_KEY)
    search_request = youtube.search().list(
        part="id",
        q=query,
        type="video",
        maxResults=50,
    )

    i = 0

    while search_request and i < max_pages:
        search_response = search_request.execute()
        video_ids = [item["id"]["videoId"] for item in search_response["items"]]

        # videos.listメソッドで動画の詳細な情報を取得
        videos_response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        yield videos_response["items"]

        search_request = youtube.search().list_next(search_request, search_response)
        i += 1

def save_to_mongodb(collection: Collection, items: List[dict]):
    """
    引数: collection: Collection, items: List[dict]
    動画の詳細な情報をMongoDBに保存する
    """
    for item in items:
        item["_id"] = item["id"]

        # sta[tisticsに含まれるviewCountプロパティなどの値が文字列になっているのでint型に変換
        for key, value in item["statistics"].items():
            item["statistics"][key] = int(value)

    # 単純にcollection.insert_many()を使うと_idが重複した場合にエラーになるので、
    # collection.bulk_write()を使う
    operations = [ReplaceOne({"_id": item["_id"]}, item, upsert=True) for item in items]
    result = collection.bulk_write(operations)
    # result = collection.insert_many(items)
    # print(f"Inserted {len(result.inserted_ids)} documents", file=sys.stderr)
    logging.info(f"Upserted {result.upserted_count} documents.")

def show_top_videos(collection: Collection):
    """
    引数: collection: Collection
    MongoDBのコレクション内でビュー数上位5件を表示する
    """
    for item in collection.find().sort("statistics.viewCount", DESCENDING).limit(5):
        print(item["statistics"]["viewCount"], item["snippet"]["title"])
        print("-" * 20)

if __name__ == '__main__':
    main()
    sys.exit(0)

