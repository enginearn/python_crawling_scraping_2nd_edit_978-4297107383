from multiprocessing.connection import Client
import lxml.html
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.scraping # db名
collection = db.books # コレクション名
collection.delete_many({})

tree = lxml.html.parse("dp.html")
html = tree.getroot()
html.make_links_absolute("https://gihyo.jp/")

for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    url = a.get("href")
    p = a.cssselect('p[itemprop="name"]')[0]
    title = p.text_content()

    collection.insert_one({"url": url, "title": title})

for link in collection.find().sort("_id"):
    print(link["_id"], link["title"], link["url"], )

client.close()
