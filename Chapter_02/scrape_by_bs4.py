from urllib.parse import urljoin
from bs4 import BeautifulSoup

html_file = "dp.html"
html_file = open(html_file, "r")
base_url = "https://gihyo.jp/dp"

soup = BeautifulSoup(html_file, "html.parser")

# with open("dp.html") as f:
#     soup = BeautifulSoup(html_file, "html.parser")

for a in soup.select('#listBook > li > a[itemprop="url"]'):
    url = urljoin(base_url, a.get("href"))
    p = a.select('p[itemprop="name"]')[0]
    title = p.text

    print(url, title)