import csv
from typing import List

import requests
import lxml.html

def main():
    """メインの処理
    fetch(), scrape(), save()の3つの関数を呼び出す
    """

    url = "https://gihyo.jp/dp"
    html = fetch(url)
    books = scrape(html, url)
    save("books.csv", books)

def fetch(url: str) -> str:
    """引数urlで与えられたURLのWebページを取得する
    WebページのencodingはContent-Typeヘッダーから取得する

    Args:
        url (str): Webサイト encodingはContent-Typeヘッダーから取得

    Returns:
        str: str型のHTML
    """

    r = requests.get(url)
    return r.text

def scrape(html: str, base_url: str) -> List[dict]:
    """引数htmlで与えられたHTMLから正規表現で書籍の情報を抜き出す
    引数base_urlは絶対URLに変換する際の基準となるURLを指定する

    Args:
        html (str): 正規表現で書籍の情報を抜き出す
        base_url (str): 絶対URLに変換する際の基準となるURL

    Returns:
        List[dict]: 書籍(dict)のリスト
    """

    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get("href")
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content()
        books.append({"url": url, "title": title})
    return books

def save(file_path: str, books: List[dict]):
    """引数booksで与えられた書籍リストをCSV形式のファイルに保存
    ファイルのパスは引数file_pathで与えられる

    Args:
        file_path (str): _description_
        books (List[dict]): なし
    """

    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, ["url", "title"])
        writer.writeheader()
        writer.writerows(books)

if __name__ == "__main__":
    main()
