import time
from typing import Iterator
import requests
import lxml.html

def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """一覧ページのResponseから
    詳細ページのURLを抜き出すジェネレーター
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get("href")
        yield url

def scrape_detail_page(response: requests.Response) -> dict:
    """詳細ページのResponseから電子書籍の情報をdictで取得する
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.text)
    ebook = {
        "url": response.url,
        "title": html.cssselect('#bookTitle')[0].text_content(),
        "price": html.cssselect('.buy')[0].text.strip(),
        "content": [h3.text_content() for h3 in html.cssselect('#content > h3')]
    }
    return ebook

def main():
    """クローラーのメイン処理
    """
    session = requests.Session()
    response = requests.get("https://gihyo.jp/dp")
    urls = scrape_list_page(response)
    for url in urls:
        time.sleep(1)
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)
        # break

if __name__ == "__main__":
    main()