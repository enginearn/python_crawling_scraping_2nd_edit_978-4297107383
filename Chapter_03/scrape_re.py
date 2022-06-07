import re
from html import unescape
from types import NoneType

file_name = "dp.html"

# WindowsでUTF-8のファイルを開く場合、明示的にencodeを指定
with open(file_name, encoding="utf-8") as f:
    html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = "http://gihyo.jp" + url
    
    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
    title = title.replace("<br/>", " ")
    title = re.sub(r"<.*?>", " ", title)
    title = unescape(title)

    print(url, title)
