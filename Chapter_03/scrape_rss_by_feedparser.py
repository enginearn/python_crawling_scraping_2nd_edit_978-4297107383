import feedparser

d = feedparser.parse("http://b.hatena.ne.jp/hotentry/it.rss")

for entry in d.entries:
    print(entry.title, entry.link)
