from typing import Iterator
from urllib import response
import requests
import lxml.html

def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """一覧ページのResponseから
    詳細ページのURLを抜き出すジェネレーター関数
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get("href")
        yield url

def main():
    """クローラーのメイン処理
    """
    response = requests.get("https://gihyo.jp/dp")
    urls = scrape_list_page(response)

    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
