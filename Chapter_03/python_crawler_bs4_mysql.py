import re
import time
from typing import Iterator
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import MySQLdb

def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """一覧ページのResponseから
    詳細ページのURLを抜き出すジェネレーター
    """
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select('#listBook > li > a[itemprop="url"]'):
        url = urljoin(response.url, a.get("href"))
        yield url

def scrape_detail_page(response: requests.Response) -> dict:
    """詳細ページのResponseから電子書籍の情報をdictで取得する
    """
    soup = BeautifulSoup(response.text, "html.parser")
    ebook = {
        "url": response.url,
        "key": extract_key(response.url),
        "title": soup.select_one('#bookTitle').text,
        "price": soup.select_one('.buy').contents[0].text.strip(),
        "content": [normalize_spaces(h3.text) for h3 in soup.select('#content > h3')]
    }
    return ebook

def extract_key(url: str) -> str:
    """URLからキー(URLの末尾のISBN)を抜き出す
    """
    m = re.search(r"/([^/]+)$", url)
    return m.group(1)

def normalize_spaces(s: str) -> str:
    """連続する空白を1つのスペースに置き換え、
    前後の空白を削除した新しい文字列を取得する
    """
    return re.sub(r"\s+", " ", s).strip()

def main():
    """クローラーのメイン処理
    """
    conn = MySQLdb.connect(db="scraping", user="scraper", port=3306,
                    passwd="password", charset="utf8mb4")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS `ebook`")
    c.execute("""
        CREATE TABLE `ebook` (
            `url` text,
            `key` text,
            `title` text,
            `price` text,
            `content` text
        )
    """)

    session = requests.Session()
    response = requests.get("https://gihyo.jp/dp")
    urls = scrape_list_page(response)
    for url in urls:
        key = extract_key(url)
        ebook = c.fetchall()
        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
            c.execute("INSERT INTO `ebook` VALUES \
                    (%(url)s, %(key)s, %(title)s, %(price)s, %(content)s)", ebook)
            conn.commit()
            print(ebook)
            # break
    conn.close()

if __name__ == "__main__":
    main()