# Python クローリング＆スクレイピング

## UNIXコマンドでのスクレイピング

<details>
<summary>wget</summary>

``` ubuntu 22.04
$ wget -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol https://gihyo.jp/dp/
```

</details>

<details>
<summary>grep</summary>

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep -E 'class="paging-number".*-'
<li class="paging-number">1 - 30 / 3450</li>
```

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep 'itemprop="name"'
<p itemprop="name" class="title"><span class="series">ゼロからはじめる</span> ゼロからはじめる<br>Facebook フ ェイスブック 基本＆<wbr>便利技</p>
<p itemprop="name" class="title"><span class="series">図解即戦力</span> 図解即戦力<br>機械業界のしくみとビジネスがこれ<wbr>1<wbr>冊でしっかりわかる教科書</p>
<p itemprop="name" class="title">分析が導く 最新<wbr>SEO<wbr>プラクティカルガイド</p>
<p itemprop="name" class="title"><span class="series">スピードマスター</span> スピードマスター<br>Access<wbr> データベース 用語図鑑</p>
```
</details>

<details>
<summary>sed</summary>

``` ubuntu 22.04
$ echo abcdefgh | sed -E 's/.*(d.).*/ \1/'
de
```

``` ubuntu 22.04
$ echo '<li class="paging-number"> 1 - 30 /  3450</li>' | sed -E 's/<[^>]*>//g'
 1 - 30 /  3450
```

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep -E 'class="paging-number".*-' | sed -E 's@. * /([0-9]+) . *@\1@'
<li class="paging-number">1 - 30 / 3450</li>
```

</details>

<details>
<summary>cut</summary>

``` ubuntu 22.04
$ echo "1,高浜岸壁,神戸市中央区東川崎町1" | cut -d , -f 2
高浜岸壁
```

</details>

<details>
<summary>awk</summary>

``` ubuntu 22.04
$ echo 'PID COMMAND %CPU TIME #TH #WQ #PORT MEM' | awk '{print $4}'
TIME
```

</details>

<details>
<summary>書籍名を取得</summary>

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep 'itemprop="name"'
<p itemprop="name" class="title"><span class="series">ゼロからはじめる</span> ゼロからはじめる<br>Facebook フ ェイスブック 基本＆<wbr>便利技</p>
<p itemprop="name" class="title"><span class="series">図解即戦力</span> 図解即戦力<br>機械業界のしくみとビジネスがこれ<wbr>1<wbr>冊でしっかりわかる教科書</p>
<p itemprop="name" class="title">分析が導く 最新<wbr>SEO<wbr>プラクティカルガイド</p>
<p itemprop="name" class="title"><span class="series">スピードマスター</span> スピードマスター<br>Access<wbr> データベース 用語図鑑</p>
```

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep 'itemprop="name"' | wc -l
30
```

``` ubuntu 22.04
$ cat gihyo.jp/dp/index.html | grep 'itemprop="name"' | sed -E 's@<br/>@ @' | sed -E 's/<[^>]*>//g'
ゼロからはじめる ゼロからはじめるFacebook フェイスブック 基本＆便利技
図解即戦力 図解即戦力機械業界のしくみとビジネスがこれ1冊でしっかりわかる教科書
分析が導く 最新SEOプラクティカルガイド
スピードマスター スピードマスターAccessデータベース 用語図鑑
動画の文法～トップ・プロが教える「伝わる動画」の作り方
今すぐ使えるかんたん 今すぐ使えるかんたんOffice for Mac［Office 2021/Microsoft 365両対応］
Software Design 2022年6月号
図解即戦力 図解即戦力自動車業界のしくみとビジネスがこれ1冊でしっかりわかる教科書
```

</details>

## Python基礎

<details>
<summary>インタプリタをクリア</summary>

os.system

``` Python 3.10
>>> import os; os.system("cls")
```

subprocess

``` Python 3.10
>>> import subprocess as sp; temp = sp.run("cls", shell=True)
```

</details>


<details>
<summary>数値</summary>

``` Python 3.10
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> 1 + 2
3
>>> 2 - 1
1
>>> 2 * 3
6
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 5 % 2
1
>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
```

</details>

<details>
<summary>文字列</summary>

``` Python 3.10
>>> type("abc")
<class 'str'>
>>> "abc"
'abc'
>>> "あいうえお"
'あいうえお'
>>> "1970's"
"1970's"
>>> print("abc\n123")
abc
123
>>> len("abc")
3
>>> len("あいうえお")
5
>>> "abcdef"[0]
'a'
>>> "abcdef"[-1]
'f'
>>> "abcdef"[1:3]
'bc'
>>> "abcdef"[:3]
'abc'
>>> "abcdef"[1:]
'bcdef'
>>> "abc" + "def"
'abcdef'
>>> message = "Hello"
>>> version = 3
>>> f"{message}, Python {version}"
'Hello, Python 3'
```

</details>


<details>
<summary>encode decode</summary>

``` Python 3.10
>>> "ABCあいうえお".encode("utf-8")
b'ABC\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
>>> type(b'ABC\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a')
<class 'bytes'>
>>> b'ABC\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'.decode("utf-8")
'ABCあいうえお'
>>> "\n ABC あいう \n".strip()
'ABC あいう'
```

</details>

<details>
<summary>list</summary>

``` Python 3.10
>>> type([])
<class 'list'>
>>> [1, 2, 3]
[1, 2, 3]
>>> [1, 2, 3,]
[1, 2, 3]
>>> [1, 2, "Three"]
[1, 2, 'Three']
>>> [1, 2, 3][0]
1
>>> [1, 2, 3][1:2]
[2]
>>> len([1, 2, 3])
3
>>> 1 in [1, 2, 3]
True
>>> [1, 2, 3].index(1)
0
>>> [1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.insert(0, 5)
>>> a
[5, 1, 2, 3, 4]
>>> del a[0]
>>> a
[1, 2, 3, 4]
>>> a.pop(0)
1
>>> a
[2, 3, 4]
>>> a[0] = 1
>>> a
[1, 3, 4]
>>> "a,b,c".split(",")
['a', 'b', 'c']
>>> ",".join(["a", "b", "c"])
'a,b,c'
```

</details>

<details>
<summary>tuple</summary>

``` Python 3.10
>>> type(())
<class 'tuple'>
>>> (1, 2)
(1, 2)
>>> (1, 2,)
(1, 2)
>>> (1,)
(1,)
>>> (1, 2, 3)[0]
1
```

</details>

<details>
<summary>dict</summary>

``` Python 3.10
>>> {"a": 1, "b": 2}
{'a': 1, 'b': 2}
>>> {"a": 1, "b": 2, 3: "c"}
{'a': 1, 'b': 2, 3: 'c'}
>>> d = dict(a=1, b=2)
>>> d
{'a': 1, 'b': 2}
>>> d["a"]
1
>>> d["c"] = 3
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>> del d["c"]
>>> d
{'a': 1, 'b': 2}
>>> "a" in d
True
>>> d["x"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'x'
>>> d.get("a")
1
>>> list(d.keys())
['a', 'b']
>>> list(d.items())
[('a', 1), ('b', 2)]
```

</details>

<details>
<summary>文字コード</summary>

encode

``` Python 3.10
>>> "あ".encode("UTF-8")
b'\xe3\x81\x82'
>>> b'\xe3\x81\x82'.decode()
'あ'
>>> "あ".encode("CP932")
b'\x82\xa0'
>>> "あ".encode("euc-jp")
b'\xa4\xa2'
```

decode

``` Python 3.10
>>> b'\xe3\x81\x82'.decode()
'あ'
```

</details>

<details>
<summary>re</summary>

search

``` Python 3.10
>>> re.search(r"a.*c", "abc123DEF")
<re.Match object; span=(0, 3), match='abc'>
>>> re.search(r"a.*d", "abc123DEF", re.IGNORECASE)
<re.Match object; span=(0, 7), match='abc123D'>
```

group

``` Python 3.10
>>> m = re.search(r"a.*c", "abc123DEF")
>>> m
<re.Match object; span=(0, 3), match='abc'>
>>> m.group()
'abc'
>>> m.group(0)
'abc'
>>> m.group(1)
'b'
```

findall

``` Python 3.10
>>> re.findall(r"\w{2,}", "This is  a Pen")
['This', 'is', 'Pen']
```

sub (substitute)

``` Python 3.10
>>> re.sub(r"\w{2,}", "That", "This is  a Pen")
'That That  a That'
```

search() と match()

``` Python 3.10
>>> re.search(r"B.*", "ABC")
<re.Match object; span=(1, 3), match='BC'>
>>> re.match(r"B.*", "ABC")
>>> # Noneが返ってきていてマッチしていない
>>> re.match(r"A.*", "ABC")
<re.Match object; span=(0, 3), match='ABC'>
```
</details>

## Requests

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> import requests
>>> r = requests.get("https://gihyo.jp/dp")
>>> type(r)
<class 'requests.models.Response'>
>>> r.status_code
200
>>> r.headers["content-type"]
'text/html; charset=UTF-8'
>>> r.encoding
'UTF-8'
>>> r.text
'<!DOCTYPE HTML>\n<html lang="ja" class="pc">\n<head>\n  <meta charset="UTF-8">\n  <title>Gihyo Digital Publishing … 技術評論社の電子書籍</title>\n  <meta http-equiv="Content-Style-Type" content="text/css"/>\n  <meta http-equiv="Content-Script-Type" content="application/javascript"/>\n  <meta name="description" content="技術評論社の電子書籍（電子出版）販売サイト"/>\n  <meta name="keywords" content="電子書籍,電子出版,EPUB,PDF,技術評論社"/>\n  <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"/>\n  <meta name="apple-mobile-web-app-capable" content="yes"/>\n  <meta name="format-detection" content="telephone=no"/>\n  <link rel="related" href="http://gihyo.jp/dp/catalogs.opds" type="application/atom+xml;profile=opds-catalog" title="Gihyo Digital Publishing OPDS Catalog"/>\n  <link rel="shortcut icon" href="/assets/templates/gdp/favicon.ico" type="image/vnd.microsoft.icon"/>\n  <link rel="apple-touch-icon-precomposed" href="/dp/assets/gdp-icon.png"/>\n  <!--[if lt IE 9]>\n    <script>var msie=8;</script>\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n    <script src="/dp/assets/js/html5shiv.min.js"></script>\n    <script src="//css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script>\n    <script src="/dp/assets/js/selectivizr-min.js"></script>\n    <script src="/dp/assets/js/addEventListener.min.js"></script>\n    <script src="/dp/assets/js/textContent.min.js"></script>\n  <![endif]-->\n  <!--[if lte IE 9]>\n    <script src="/dp/assets/js/classList.min.js" defer></script>\n  <![endif]-->\n  <link rel="stylesheet" href="/dp/assets/style/store0902.css" type="text/css" media="all"/>\n  <script src="/dp/assets/js/gdpFunction0425.min.js" defer></script>\n  <meta name="twitter:card" content="summary_large_image"/>\n  <meta name="twitter:site" content="@gihyoDP"/>\n  <meta property="og:title" content="Gihyo Digital Publishing … 技術評論社の電子書籍"/>\n  <meta property="og:type" content="website"/>\n  <meta property="og:description" content="技術評論社の電子書籍（電子出版）販売サイト"/>\n 
```

</details>

<details>
<summary>高度な機能</summary>

``` Python 3.10
>>> r = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010")
>>> r.status_code
200
>>> r.json()
Traceback (most recent call last):
  File "C:\Users\path	o\Development\Python\crawling_scraping_2nd_edit\venv\lib\site-packages\requests\models.py", line 910, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Python310\lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Python310\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Python310\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 2 column 1 (char 4)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\path	o\Development\Python\crawling_scraping_2nd_edit\venv\lib\site-packages\requests\models.py", line 917, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: [Errno Expecting value]
<!DOCTYPE html>
<html lang="ja">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WPKMK2X');</script>
<!-- End Google Tag Manager -->
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9">
<meta charset="utf-8">
<title>livedoor</title>
<meta name="description" content="LINE株式会社が運営するポータルサイト。速報性に加え独自の切り口を誇る「ライブドアニュース」、日本最大のブログサービス「ライブドアブログ」ほか、厳選した情報をお届けします。">
<meta name="keywords" content="ライブドア,ポータル,ニュース,ブログ,livedoor,portal,LINE,LD">
<meta property="og:site_name" content="livedoor">
<meta property="og:image" content="https://image.livedoor.com/img/top/17/livedoor_small.png">
<meta name="verify-v1" content="1bivxaxGrLBSoWSu7qAOa0M36HWHyewW+8YqCFDlBZQ=">

<link rel="shortcut icon" href="/img/ie9/favicon.ico">

<style type="text/css">
```

``` Python 3.10
>>> r = requests.post("http://httpbin.org/post", data={"key1": "value"})
>>> r = requests.get("http://httpbin.org/get", headers={"user-agent": "my-crawler/1.0(+foo@example.com)"})
>>> r
<Response [200]>
>>> r.headers
{'Date': 'Tue, 24 May 2022 01:44:05 GMT', 'Content-Type': 'application/json', 'Content-Length': '317', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
>>> r = requests.get("https://api.github.com/user", auth=("github account", "github passwd"))
>>> r
<Response [401]>
>>> r = requests.get("http://httpbin.org/get", params={"key": "value1"})
```

``` Python 3.10
>>> s = requests.Session()
>>> s.headers.update({"user-agent": "my-crawler/1.0(+foo@example.com)"})
>>> r = s.get("https://gihyo.jp/")
>>> r = s.get("https://gihyo.jp/dp")
```

</details>

## lxml

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> import lxml.html
>>> tree = lxml.html.parse("dp.html")
>>> tree
<lxml.etree._ElementTree object at 0x00000214E1EECAC0>
>>> type(tree)
<class 'lxml.etree._ElementTree'>
>>> html = tree.getroot()
>>> type(html)
<class 'lxml.html.HtmlElement'>
>>> html = lxml.html.fromstring("""
... <html>
... <head><title>八百屋オンライン</title></head>
... <body>
...  <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
... <ul>
...   <li>りんご</li>
...   <li class="featured">みかん</li>
...   <li>ぶどう</li>
... </ul>
... </body>
... </html>""")
>>> type(html)
<class 'lxml.html.HtmlElement'>
>>> html.xpath("//li")
[<Element li at 0x214e23ae340>, <Element li at 0x214e23ae390>, <Element li at 0x214e23ae3e0>]
>>> html.cssselect("li")
[<Element li at 0x214e23ae340>, <Element li at 0x214e23ae390>, <Element li at 0x214e23ae3e0>]
>>> h1.get("id")
'main'
>>> h1.attrib
{'id': 'main'}
>>> h1.getparent()
<Element body at 0x214e23ae390>
>>> strong.text
'おいしい'
>>> strong.tail
'今日のくだもの'
>>> h1.text_content()
'おいしい今日のくだもの'
```

</details>

<details>
<summary>lxml.etree</summary>

``` Python 3.10
>>> import lxml.etree
>>> import requests
>>> url = "https://gihyo.jp/feed/atom"
>>> src = requests.get(url)
>>> tree = lxml.etree.parse(src.text)

```

</details>

## urllib

<details>
<summary>urljoin</summary>

``` Python 3.10
>>> from urllib.parse import urljoin
>>> base_url = "http://example.com/books/top.html"
>>> urljoin(base_url, "//cdn.example.com/logo.png")
'http://cdn.example.com/logo.png'
>>> urljoin(base_url, "/articles/")
'http://example.com/articles/'
>>> urljoin(base_url, "/books/")
'http://example.com/books/'
```

</details>

<details>
<summary>robotparser</summary>

``` Python 3.10
>>> import urllib.robotparser
>>> rp = urllib.robotparser.RobotFileParser()
>>> rp.set_url("https://www.python.org/robots.txt")
>>> rp.read()
>>> rp.can_fetch("mybot", "https://www.python.org/")
True
```

</details>

## BeautifulSoup4

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> from bs4 import BeautifulSoup
>>> with open("dp.html") as f:
...     soup = BeautifulSoup(f, "html.parser")
...
>>> soup
<!DOCTYPE HTML>

<html class="pc" lang="ja">
<head>
<meta charset="utf-8"/>
<title>Gihyo Digital Publishing … 技術評論社の電子書籍</title>
```

``` Python 3.10
>>> soup = BeautifulSoup("""
... <html>
... ... <head><title>八百屋オンライン</title></head>
... ... <body>
... ...  <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
... ... <ul>
... ...   <li>りんご</li>
... ...   <li class="featured">みかん</li>
... ...   <li>ぶどう</li>
... ... </ul>
... ... </body>
... ... </html>""", "html.parser")
>>> soup.h1
<h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
>>> soup.title
<title>八百屋オンライン</title>
>>> type(soup.title)
<class 'bs4.element.Tag'>
>>> soup.title.name
'title'
>>> soup.title.string
'八百屋オンライン'
>>> type(soup.title.string)
<class 'bs4.element.NavigableString'>
>>> soup.h1.string
>>> soup.h1.contents
[<strong>おいしい</strong>, '今日のくだもの']
>>> soup.h1.text
'おいしい今日のくだもの'
>>> type(soup.h1.text)
<class 'str'>
>>> soup.h1["id"] 
'main'
>>> soup.h1.get("id")
'main'
>>> soup.h1.attrs
{'id': 'main'}
>>> soup.h1.parent
<body>
...  <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
... <ul>
...   <li>りんご</li>
...   <li class="featured">みかん</li>
...   <li>ぶどう</li>
... </ul>
... </body>
>>> soup.li
<li>りんご</li>
>>> soup.find("li")
<li>りんご</li>
>>> soup.find_all("li")
[<li>りんご</li>, <li class="featured">みかん</li>, <li>ぶどう</li>]
>>> soup.find_all("li", class_="featured")
[<li class="featured">みかん</li>]
>>> soup.find_all(id="main")
[<h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>]
>>> soup.select("li")
[<li>りんご</li>, <li class="featured">みかん</li>, <li>ぶどう</li>]
>>> soup.select("li.featured")
[<li class="featured">みかん</li>]
>>> soup.select("#main")
[<h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>]
```

</details>

## pyquery

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> from pyquery import PyQuery as pq
>>> d = pq(filename="index.html")
>>> d = pq(url="http://example.com/")
>>> d
[<html>]
>>> d = pq("""
... <html>
... ... <head><title>八百屋オンライン</title></head>
... ...   <body>
... ... ... <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
... ... ... <ul>
... ... ...   <li>りんご</li>
... ... ...   <li class="featured">みかん</li>
... ... ...   <li>ぶどう</li>
... ... ... </ul>
... ... ..</body>
... </html>""")
>>> d("h1")
[<h1#main>]
>>> type(d("h1"))
<class 'pyquery.pyquery.PyQuery'>
>>> type(d("h1"))
<class 'pyquery.pyquery.PyQuery'>
>>> d("h1")
[<h1#main>]
>>> d("h1")[0]
<Element h1 at 0x206302803c0>
>>> d("h1").text()
'おいしい今日のくだもの'
>>> d("h1").attr("id")
'main'
>>> d("h1").attr.id
'main'
>>> d("h1").attr["id"]
'main'
>>> d("h1").children()
[<strong>]
>>> d("h1").parent()
[<body>]
>>> d("li")
[<li>, <li.featured>, <li>]
>>> d("li.featured")
[<li.featured>]
>>> d("#main")
[<h1#main>]
>>> d("body").find("li")
[<li>, <li.featured>, <li>]
>>> d("li").filter(".featured")
[<li.featured>]
>>> d("li").eq(1)
[<li.featured>]
```

</details>

## RSS feedparser

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> import feedparser
>>> d = feedparser.parse("http://b.hatena.ne.jp/hotentry/it.rss")
>>> d = feedparser.parse("it.rss")
>>> type(d)
<class 'feedparser.util.FeedParserDict'>
>>> d.version
'rss10'
>>> d.feed.title
'はてなブックマーク - 人気エントリー - テクノロジー'
>>> d["feed"]["title"]
'はてなブックマーク - 人気エントリー - テクノロジー'
>>> d.feed.link
'https://b.hatena.ne.jp/hotentry/it'
>>> d.feed.description
'最近の人気エントリー'
>>> len(d.entries)
30
>>> d.entries[0].title
'Dockerのことが多分わかるハンズオン'
>>> d.entries[0].link
'https://speakerdeck.com/yoshi0202/dockerfalsekotogaduo-fen-wakaruhanzuon'
>>> d.entries[0].description
'Transcript Dockerのことが 多分わかるハンズオン Yoshiki Kobayashi 2020/06/28 Hello World!! 自称なんでも屋。好きなAWSのサービスはLambda。 好きな言語はJavaScriptとRuby。Nintendo Switch難民。 最近転職しました。 Name : Yoshiki Kobayashi @yoshi0202 @codeplumdev https://code-plum.dev モダンな技術って 憧...'
>>> d.entries[0].updated
'2022-06-04T03:06:37Z'
>>> d.entries[0].updated_parsed
time.struct_time(tm_year=2022, tm_mon=6, tm_mday=4, tm_hour=3, tm_min=6, tm_sec=37, tm_wday=5, tm_yday=155, tm_isdst=0)
```

</details>

## MySQL

<details>
<summary>CREATE DB</summary>

``` MySQL 8
mysql> create database scraping default character set utf8mb4;
Query OK, 1 row affected (0.06 sec)
```

</details>

<details>
<summary>CREATE USER</summary></summary>

``` MySQL 8
mysql> create user "scraper"@"%" identified by "password";　# どこからでもアクセスOK %はwildcard
Query OK, 0 rows affected (0.09 sec)
```

</details>

<details>
<summary>GRANT</summary>

``` MySQL 8
mysql> grant all on scraping.* to "scraper"@"%";
Query OK, 0 rows affected, 1 warning (0.02 sec)
```

</details>

## Mongo DB

<details>
<summary>基本的な使い方</summary>

``` Python 3.10
>>> from pymongo import MongoClient
>>> client = MongoClient("localhost", 27017)
>>> db = client.test
>>> db = client["test"]
>>> collection = db.spots
>>> collection = db["spots"]
>>> collection.insert_one({"name": "東京スカイツリー", "prefecture": "東京"})
<pymongo.results.InsertOneResult object at 0x000001B2BF877460>
>>> collection.insert_many([{"name": "東京ディズニーランド", "prefecture": "千葉"}, {"name": "東京ドーム", "prefecture": "東京"}])
<pymongo.results.InsertManyResult object at 0x000001B2BF877280>
>>> for spot in collection.find():
...     print(spot)
...
{'_id': ObjectId('629d4c8a7c4bd6e36e49f193'), 'name': '東京スカイツリー', 'prefecture': '東京'}
{'_id': ObjectId('629d4d657c4bd6e36e49f194'), 'name': '東京ディズニーランド'}
{'_id': ObjectId('629d4d657c4bd6e36e49f195'), 'name': '東京ドーム', 'prefecture': '東京'}
>>> collection.find_one()
{'_id': ObjectId('629d4c8a7c4bd6e36e49f193'), 'name': '東京スカイツリー', 'prefecture': '東京'}
>>> collection.find_one({"prefecture": "千葉"})
{'_id': ObjectId('629d4e4d7c4bd6e36e49f196'), 'name': '東京ディズニーランド', 'prefecture': '千葉'}
>>> for spot in collection.find():
...     print(spot)
...
{'_id': ObjectId('629d4c8a7c4bd6e36e49f193'), 'name': '東京スカイツリー', 'prefecture': '東京'}
{'_id': ObjectId('629d4e4d7c4bd6e36e49f196'), 'name': '東京ディズニーランド', 'prefecture': '千葉'}
{'_id': ObjectId('629d4d657c4bd6e36e49f195'), 'name': '東京ドーム', 'prefecture': '東京'}
```

</details>

## Pandas

<details>
<summary>基本的な使い方</summary>

`Series`は1次元のラベル付き配列。

``` Python 3.10

``` Python 3.10
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> s1 = pd.Series([4, -2, 5])
>>> s1
0    4
1   -2
2    5
dtype: int64
>>> s1.index
RangeIndex(start=0, stop=3, step=1)
>>> list(s1.index)
[0, 1, 2]
>>> s1.values
array([ 4, -2,  5], dtype=int64)
>>> list(s1.values)
[4, -2, 5]
>>> s2 = pd.Series([4, -2, 5], index=["a", "b", "c"])
>>> s2
a    4
b   -2
c    5
dtype: int64
>>> s2.index
Index(['a', 'b', 'c'], dtype='object')
>>> s2['a']
4
>>> s2.a
4
>>> s2['c'] = 2
>>> s2
a    4
b   -2
c    2
dtype: int64
```

`DataFrame`は2次元の表形式の配列。

``` Python 3.10
>>> df = pd.DataFrame({'math': [78, 64, 53], 'english': [45, 87, 67]}, index=['001', '002', '003'], columns=['math', 'english'])
>>> df
     math  english
001    78       45
002    64       87
003    53       67
>>> df['math']        
001    78
002    64
003    53
Name: math, dtype: int64
>>> df.english    
001    45
002    87
003    67
Name: english, dtype: int64
>>> df.loc['001']
math       78
english    45
Name: 001, dtype: int64
>>> df.iloc[0]    
math       78
english    45
Name: 001, dtype: int64
>>> df.english['001']
45
>>> df.describe()
            math    english
count   3.000000   3.000000
mean   65.000000  66.333333
std    12.529964  21.007935
min    53.000000  45.000000
25%    58.500000  56.000000
50%    64.000000  67.000000
75%    71.000000  77.000000
max    78.000000  87.000000
>>> df.to_csv('score.csv')
```

`read_csv`

``` Python 3.10
>>> pd.read_csv('exchange.csv', encoding='CP932')
      データコード               FM08'FXERM07 FM09'FX180110002
0       系列名称  東京市場　ドル・円　スポット　17時時点/月中平均      実質実効為替レート指数
1    1970/01                        NaN            58.32
2    1970/02                        NaN            57.98
3    1970/03                        NaN            58.19
4    1970/04                        NaN            58.25
..       ...                        ...              ...
632  2022/08                        NaN              NaN
633  2022/09                        NaN              NaN
634  2022/10                        NaN              NaN
635  2022/11                        NaN              NaN
636  2022/12                        NaN              NaN

[637 rows x 3 columns]
>>> df_exchange = pd.read_csv('exchange.csv', encoding='CP932', header=1, names=['data', 'USD', 'rate'], index_col=0, parse_dates=True)
>>> df_exchange
            USD   rate
data
1970-01-01  NaN  58.32
1970-02-01  NaN  57.98
1970-03-01  NaN  58.19
1970-04-01  NaN  58.25
1970-05-01  NaN  57.85
...         ...    ...
2022-08-01  NaN    NaN
2022-09-01  NaN    NaN
2022-10-01  NaN    NaN
2022-11-01  NaN    NaN
2022-12-01  NaN    NaN

[636 rows x 2 columns]
```

``` Python 3.10
>>> df_exchange.rate[0]
58.32
>>> type(df_exchange.rate[0]) 
<class 'numpy.float64'>
```

元号を西暦へ変換する関数

``` Python 3.10

``` Python 3.10
>>> from datetime import datetime
>>> def parse_japanese_date(s):
...     base_years = {'E': 1596, 'M': 1868, 'T': 1912, 'S': 1925, 'H': 1988, 'R': 2018}
...     era = s[0]
...     year, month, day = s[1:].split('.') 
...     year = base_years[era] + int(year)
...     return datetime(year, int(month), int(day))
... 
>>> parse_japanese_date('S49.9.24')
datetime.datetime(1974, 9, 24, 0, 0)
>>> parse_japanese_date('E49.9.24')
datetime.datetime(1645, 9, 24, 0, 0)
>>> parse_japanese_date('R20.9.24') 
datetime.datetime(2038, 9, 24, 0, 0)
```

``` Python 3.10

```
</details>

<details>
<summary>read_csv</summary>

``` Python 3.10
>>> df_jgbcm = pd.read_csv('jgbcm_all.csv', encoding='CP932', header=1, index_col=0, parse_dates=True, date_parser=parse_japanese_date, na_values=['-']) 
>>> df_jgbcm
                1年     2年     3年     4年     5年     6年     7年     8年     9年    10年    15年    20年    25年    30年    40年
基準日
1974-09-24  10.327  9.362  8.830  8.515  8.348  8.290  8.240  8.121  8.127    NaN    NaN    NaN    NaN    NaN    NaN
1974-09-25  10.333  9.364  8.831  8.516  8.348  8.290  8.240  8.121  8.127    NaN    NaN    NaN    NaN    NaN    NaN
1974-09-26  10.340  9.366  8.832  8.516  8.348  8.290  8.240  8.122  8.128    NaN    NaN    NaN    NaN    NaN    NaN
1974-09-27  10.347  9.367  8.833  8.517  8.349  8.290  8.240  8.122  8.128    NaN    NaN    NaN    NaN    NaN    NaN
1974-09-28  10.354  9.369  8.834  8.518  8.349  8.291  8.240  8.122  8.129    NaN    NaN    NaN    NaN    NaN    NaN
...            ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...
2022-06-24  -0.133 -0.079 -0.047 -0.017  0.049  0.106  0.157  0.220  0.244  0.240  0.634  0.897  1.099  1.211  1.284
2022-06-27  -0.115 -0.066 -0.037 -0.007  0.061  0.121  0.176  0.240  0.258  0.252  0.659  0.922  1.130  1.250  1.320
2022-06-28  -0.114 -0.045 -0.027  0.003  0.068  0.126  0.182  0.245  0.263  0.252  0.664  0.929  1.135  1.257  1.337
2022-06-29  -0.114 -0.050 -0.034 -0.002  0.056  0.116  0.167  0.230  0.254  0.246  0.650  0.911  1.118  1.240  1.325
2022-06-30  -0.105 -0.065 -0.057 -0.022  0.042  0.107  0.167  0.235  0.253  0.242  0.634  0.891  1.083  1.213  1.294

[12271 rows x 15 columns]
```

</details>

<details>
<summary>read_excel</summary>

- `sheet_name`を指定して読み込む。複数のシートを読み込む時は`list`でシート名を指定。

  - eg. `sheet_name=['sheet1', 'sheet2']`

- `skiprows`を指定して行を読み飛ばす。`list`で指定する。

  - eg. `skiprows=[0,1,2,4]`

    `slice`は指定できない。`skiprows=[:3,4]` はエラーになる。

- `skipfooter`を指定して最後の行を読み飛ばす。`int`で指定する。
  - eg. `skipfooter=1`

- `'usecols' must either be list-like of all strings, all unicode, all integers or a callable.`
  - eg. `usecols=['A', 'B', 'C']`

``` Python 3.10
>>> import pandas as pd
>>> df_jobs = pd.read_excel("third_table.xlsx", sheet_name=0, skiprows=[0,1,2,4], skipfooter=3, usecols="A,U:AF", index_col=0)
>>> df_jobs.columns = [c.split(".")[0] for c in df_jobs.columns]
>>> df_jobs
         １月    ２月    ３月    ４月    ５月    ６月    ７月    ８月    ９月   10月   11月   12月
西暦
1963年  0.56  0.60  0.64  0.68  0.71  0.80  0.77  0.72  0.71  0.71  0.72  0.73
1964年  0.75  0.76  0.76  0.79  0.81  0.83  0.83  0.82  0.83  0.81  0.79  0.78
1965年  0.74  0.71  0.71  0.70  0.66  0.63  0.60  0.58  0.57  0.57  0.56  0.55
1966年  0.58  0.62  0.67  0.70  0.71  0.73  0.72  0.78  0.82  0.85  0.85  0.85
1967年  0.87  0.90  0.91  0.94  0.97  1.00  1.02  1.08  1.09  1.09  1.11  1.10
1968年  1.11  1.09  1.08  1.07  1.09  1.10  1.11  1.12  1.14  1.14  1.17  1.17
1969年  1.19  1.20  1.21  1.24  1.25  1.29  1.30  1.33  1.34  1.39  1.41  1.46
1970年  1.49  1.47  1.44  1.43  1.43  1.44  1.41  1.39  1.39  1.36  1.33  1.31
1971年  1.29  1.23  1.21  1.18  1.15  1.10  1.09  1.07  1.03  1.02  1.00  0.99
1972年  0.98  1.02  1.05  1.07  1.08  1.09  1.13  1.19  1.25  1.31  1.36  1.48
1973年  1.60  1.65  1.61  1.63  1.74  1.82  1.87  1.86  1.83  1.86  1.93  1.84
1974年  1.64  1.53  1.45  1.34  1.35  1.27  1.18  1.09  1.02  0.95  0.88  0.79
1975年  0.75  0.71  0.67  0.68  0.63  0.59  0.56  0.55  0.55  0.55  0.55  0.55
1976年  0.58  0.61  0.63  0.65  0.64  0.66  0.67  0.67  0.66  0.64  0.64  0.62
1977年  0.61  0.60  0.60  0.61  0.56  0.54  0.53  0.53  0.53  0.53  0.52  0.52
1978年  0.51  0.53  0.54  0.57  0.54  0.54  0.56  0.57  0.59  0.59  0.60  0.60
1979年  0.62  0.63  0.66  0.70  0.69  0.71  0.72  0.73  0.75  0.77  0.78  0.79
1980年  0.77  0.76  0.77  0.77  0.76  0.77  0.76  0.74  0.73  0.73  0.71  0.70
1981年  0.69  0.68  0.67  0.67  0.67  0.68  0.70  0.69  0.68  0.67  0.66  0.67
1982年  0.66  0.65  0.63  0.62  0.60  0.60  0.60  0.60  0.60  0.60  0.59  0.59
1983年  0.59  0.59  0.59  0.59  0.59  0.59  0.59  0.60  0.61  0.62  0.62  0.63
1984年  0.64  0.64  0.64  0.64  0.64  0.64  0.65  0.65  0.66  0.66  0.66  0.67
1985年  0.68  0.69  0.68  0.69  0.69  0.69  0.69  0.68  0.68  0.67  0.67  0.67
1986年  0.67  0.66  0.65  0.63  0.62  0.60  0.60  0.61  0.61  0.61  0.61  0.61
1987年  0.62  0.63  0.64  0.64  0.65  0.66  0.68  0.71  0.74  0.77  0.81  0.84
1988年  0.87  0.90  0.92  0.95  0.98  1.01  1.04  1.06  1.08  1.10  1.12  1.14
1989年  1.15  1.17  1.17  1.19  1.25  1.27  1.30  1.29  1.30  1.31  1.33  1.33
1990年  1.33  1.36  1.36  1.35  1.39  1.42  1.46  1.44  1.44  1.44  1.45  1.44
1991年  1.43  1.44  1.44  1.41  1.44  1.44  1.44  1.40  1.36  1.36  1.34  1.31
1992年  1.25  1.22  1.19  1.14  1.13  1.10  1.08  1.05  1.02  0.99  0.96  0.93
1993年  0.91  0.88  0.85  0.82  0.80  0.76  0.74  0.72  0.70  0.68  0.67  0.66
1994年  0.65  0.64  0.65  0.65  0.63  0.63  0.63  0.64  0.65  0.65  0.64  0.63
1995年  0.64  0.65  0.66  0.65  0.63  0.62  0.61  0.62  0.62  0.62  0.62  0.63
1996年  0.65  0.66  0.68  0.69  0.69  0.70  0.72  0.72  0.72  0.73  0.74  0.74
1997年  0.74  0.74  0.74  0.74  0.74  0.74  0.74  0.73  0.71  0.70  0.68  0.67
1998年  0.63  0.61  0.57  0.56  0.54  0.52  0.51  0.50  0.49  0.48  0.47  0.47
1999年  0.48  0.48  0.48  0.47  0.46  0.46  0.47  0.47  0.48  0.49  0.49  0.50
2000年  0.51  0.52  0.54  0.56  0.56  0.58  0.60  0.61  0.62  0.64  0.65  0.65
2001年  0.65  0.64  0.63  0.62  0.61  0.61  0.60  0.58  0.57  0.54  0.52  0.51
2002年  0.50  0.51  0.52  0.52  0.53  0.53  0.54  0.55  0.55  0.56  0.56  0.57
2003年  0.58  0.59  0.60  0.61  0.61  0.62  0.63  0.65  0.67  0.70  0.72  0.75
2004年  0.76  0.76  0.77  0.78  0.80  0.82  0.83  0.84  0.86  0.88  0.91  0.92
2005年  0.91  0.91  0.93  0.94  0.94  0.95  0.96  0.96  0.96  0.98  0.99  1.01
2006年  1.03  1.04  1.05  1.05  1.07  1.07  1.08  1.07  1.07  1.06  1.06  1.06
2007年  1.06  1.05  1.05  1.07  1.07  1.07  1.06  1.05  1.03  1.01  0.98  0.98
2008年  0.97  0.96  0.96  0.96  0.95  0.92  0.89  0.86  0.83  0.79  0.75  0.71
2009年  0.64  0.57  0.52  0.49  0.46  0.44  0.43  0.42  0.43  0.44  0.44  0.44
2010年  0.45  0.46  0.48  0.49  0.50  0.51  0.53  0.54  0.55  0.56  0.58  0.59
2011年  0.60  0.62  0.62  0.62  0.61  0.62  0.64  0.65  0.67  0.69  0.71  0.72
2012年  0.74  0.75  0.77  0.78  0.79  0.80  0.81  0.82  0.81  0.82  0.82  0.83
2013年  0.84  0.85  0.87  0.88  0.90  0.92  0.93  0.95  0.96  0.99  1.01  1.03
2014年  1.04  1.06  1.07  1.08  1.09  1.09  1.10  1.10  1.10  1.11  1.12  1.14
2015年  1.15  1.16  1.16  1.16  1.18  1.19  1.20  1.22  1.23  1.24  1.26  1.27
2016年  1.29  1.30  1.31  1.33  1.35  1.36  1.36  1.38  1.38  1.40  1.41  1.42
2017年  1.43  1.45  1.45  1.48  1.49  1.50  1.51  1.52  1.53  1.55  1.56  1.58
2018年  1.60  1.59  1.59  1.59  1.60  1.61  1.63  1.63  1.64  1.63  1.63  1.63
2019年  1.63  1.63  1.62  1.62  1.62  1.60  1.59  1.60  1.59  1.59  1.57  1.57
2020年  1.49  1.45  1.39  1.31  1.18  1.12  1.08  1.05  1.04  1.05  1.05  1.06
2021年  1.08  1.09  1.10  1.09  1.10  1.13  1.14  1.15  1.15  1.16  1.17  1.17
2022年  1.20  1.21  1.22  1.23  1.24   NaN   NaN   NaN   NaN   NaN   NaN   NaN
```

`stack()`で2次元の`DataFrame`を1次元の`Series`に変換する。

``` Python 3.10
>>> s_jobs= df_jobs.stack()
>>> s_jobs
西暦
1963年  １月    0.56
       ２月    0.60
       ３月    0.64
       ４月    0.68
       ５月    0.71
             ...
2022年  １月    1.20
       ２月    1.21
       ３月    1.22
       ４月    1.23
       ５月    1.24
Length: 713, dtype: float64
```

`stack()`で`MultiIndex`になる。

``` Python 3.10
>>> s_jobs.index
MultiIndex([('1963年',  '１月'),
            ('1963年',  '２月'),
            ('1963年',  '３月'),
            ('1963年',  '４月'),
            ('1963年',  '５月'),
            ('1963年',  '６月'),
            ('1963年',  '７月'),
            ('1963年',  '８月'),
            ('1963年',  '９月'),
            ('1963年', '10月'),
            ...
            ('2021年',  '８月'),
            ('2021年',  '９月'),
            ('2021年', '10月'),
            ('2021年', '11月'),
            ('2021年', '12月'),
            ('2022年',  '１月'),
            ('2022年',  '２月'),
            ('2022年',  '３月'),
            ('2022年',  '４月'),
            ('2022年',  '５月')],
           names=['西暦', None], length=713)
```

`unstack()`で`DataFrame`に戻せる。

``` Python 3.10
>>> s_jobs.unstack()
         ３月    ５月    ６月    ７月    ８月    ９月   10月   11月   12月  1～3月平均  4～6月平均  7～9月平均  10～12月平均
西暦
1963年  0.64  0.71  0.80  0.77  0.72  0.71  0.71  0.72  0.73    0.60    0.73    0.73      0.72
1964年  0.76  0.81  0.83  0.83  0.82  0.83  0.81  0.79  0.78    0.76    0.81    0.83      0.79
1965年  0.71  0.66  0.63  0.60  0.58  0.57  0.57  0.56  0.55    0.72    0.66    0.58      0.56
1966年  0.67  0.71  0.73  0.72  0.78  0.82  0.85  0.85  0.85    0.62    0.71    0.77      0.85
1967年  0.91  0.97  1.00  1.02  1.08  1.09  1.09  1.11  1.10    0.89    0.97    1.06      1.10
1968年  1.08  1.09  1.10  1.11  1.12  1.14  1.14  1.17  1.17    1.09    1.09    1.13      1.16
1969年  1.21  1.25  1.29  1.30  1.33  1.34  1.39  1.41  1.46    1.20    1.26    1.32      1.42
1970年  1.44  1.43  1.44  1.41  1.39  1.39  1.36  1.33  1.31    1.47    1.43    1.40      1.34
1971年  1.21  1.15  1.10  1.09  1.07  1.03  1.02  1.00  0.99    1.24    1.14    1.06      1.00
1972年  1.05  1.08  1.09  1.13  1.19  1.25  1.31  1.36  1.48    1.02    1.08    1.19      1.38
1973年  1.61  1.74  1.82  1.87  1.86  1.83  1.86  1.93  1.84    1.62    1.73    1.85      1.87
1974年  1.45  1.35  1.27  1.18  1.09  1.02  0.95  0.88  0.79    1.54    1.32    1.10      0.87
1975年  0.67  0.63  0.59  0.56  0.55  0.55  0.55  0.55  0.55    0.71    0.63    0.56      0.55
1976年  0.63  0.64  0.66  0.67  0.67  0.66  0.64  0.64  0.62    0.61    0.65    0.67      0.63
1977年  0.60  0.56  0.54  0.53  0.53  0.53  0.53  0.52  0.52    0.60    0.57    0.53      0.52
1978年  0.54  0.54  0.54  0.56  0.57  0.59  0.59  0.60  0.60    0.53    0.55    0.57      0.60
1979年  0.66  0.69  0.71  0.72  0.73  0.75  0.77  0.78  0.79    0.64    0.70    0.73      0.78
1980年  0.77  0.76  0.77  0.76  0.74  0.73  0.73  0.71  0.70    0.77    0.77    0.75      0.72
1981年  0.67  0.67  0.68  0.70  0.69  0.68  0.67  0.66  0.67    0.68    0.67    0.69      0.67
1982年  0.63  0.60  0.60  0.60  0.60  0.60  0.60  0.59  0.59    0.65    0.60    0.60      0.59
1983年  0.59  0.59  0.59  0.59  0.60  0.61  0.62  0.62  0.63    0.59    0.59    0.60      0.62
1984年  0.64  0.64  0.64  0.65  0.65  0.66  0.66  0.66  0.67    0.64    0.64    0.65      0.66
1985年  0.68  0.69  0.69  0.69  0.68  0.68  0.67  0.67  0.67    0.68    0.69    0.68      0.67
1986年  0.65  0.62  0.60  0.60  0.61  0.61  0.61  0.61  0.61    0.66    0.62    0.60      0.61
1987年  0.64  0.65  0.66  0.68  0.71  0.74  0.77  0.81  0.84    0.63    0.65    0.71      0.80
1988年  0.92  0.98  1.01  1.04  1.06  1.08  1.10  1.12  1.14    0.90    0.98    1.06      1.12
1989年  1.17  1.25  1.27  1.30  1.29  1.30  1.31  1.33  1.33    1.16    1.24    1.29      1.32
1990年  1.36  1.39  1.42  1.46  1.44  1.44  1.44  1.45  1.44    1.35    1.39    1.45      1.44
1991年  1.44  1.44  1.44  1.44  1.40  1.36  1.36  1.34  1.31    1.44    1.43    1.40      1.34
1992年  1.19  1.13  1.10  1.08  1.05  1.02  0.99  0.96  0.93    1.22    1.12    1.05      0.96
1993年  0.85  0.80  0.76  0.74  0.72  0.70  0.68  0.67  0.66    0.88    0.79    0.72      0.67
1994年  0.65  0.63  0.63  0.63  0.64  0.65  0.65  0.64  0.63    0.65    0.64    0.64      0.64
1995年  0.66  0.63  0.62  0.61  0.62  0.62  0.62  0.62  0.63    0.65    0.63    0.62      0.63
1996年  0.68  0.69  0.70  0.72  0.72  0.72  0.73  0.74  0.74    0.66    0.70    0.72      0.74
1997年  0.74  0.74  0.74  0.74  0.73  0.71  0.70  0.68  0.67    0.74    0.74    0.73      0.68
1998年  0.57  0.54  0.52  0.51  0.50  0.49  0.48  0.47  0.47    0.60    0.54    0.50      0.48
1999年  0.48  0.46  0.46  0.47  0.47  0.48  0.49  0.49  0.50    0.48    0.47    0.47      0.49
2000年  0.54  0.56  0.58  0.60  0.61  0.62  0.64  0.65  0.65    0.53    0.57    0.61      0.65
2001年  0.63  0.61  0.61  0.60  0.58  0.57  0.54  0.52  0.51    0.64    0.61    0.58      0.52
2002年  0.52  0.53  0.53  0.54  0.55  0.55  0.56  0.56  0.57    0.51    0.53    0.55      0.57
2003年  0.60  0.61  0.62  0.63  0.65  0.67  0.70  0.72  0.75    0.59    0.61    0.65      0.73
2004年  0.77  0.80  0.82  0.83  0.84  0.86  0.88  0.91  0.92    0.76    0.80    0.84      0.90
2005年  0.93  0.94  0.95  0.96  0.96  0.96  0.98  0.99  1.01    0.92    0.94    0.96      0.99
2006年  1.05  1.07  1.07  1.08  1.07  1.07  1.06  1.06  1.06    1.04    1.06    1.07      1.06
2007年  1.05  1.07  1.07  1.06  1.05  1.03  1.01  0.98  0.98    1.05    1.07    1.05      0.99
2008年  0.96  0.95  0.92  0.89  0.86  0.83  0.79  0.75  0.71    0.96    0.94    0.86      0.75
2009年  0.52  0.46  0.44  0.43  0.42  0.43  0.44  0.44  0.44    0.58    0.46    0.43      0.44
2010年  0.48  0.50  0.51  0.53  0.54  0.55  0.56  0.58  0.59    0.47    0.50    0.54      0.58
2011年  0.62  0.61  0.62  0.64  0.65  0.67  0.69  0.71  0.72    0.61    0.61    0.65      0.71
2012年  0.77  0.79  0.80  0.81  0.82  0.81  0.82  0.82  0.83    0.75    0.79    0.81      0.82
2013年  0.87  0.90  0.92  0.93  0.95  0.96  0.99  1.01  1.03    0.86    0.90    0.95      1.01
2014年  1.07  1.09  1.09  1.10  1.10  1.10  1.11  1.12  1.14    1.06    1.09    1.10      1.12
2015年  1.16  1.18  1.19  1.20  1.22  1.23  1.24  1.26  1.27    1.16    1.18    1.22      1.25
2016年  1.31  1.35  1.36  1.36  1.38  1.38  1.40  1.41  1.42    1.30    1.35    1.37      1.41
2017年  1.45  1.49  1.50  1.51  1.52  1.53  1.55  1.56  1.58    1.44    1.49    1.52      1.57
2018年  1.59  1.60  1.61  1.63  1.63  1.64  1.63  1.63  1.63    1.59    1.60    1.63      1.63
2019年  1.62  1.62  1.60  1.59  1.60  1.59  1.59  1.57  1.57    1.63    1.62    1.59      1.58
2020年  1.39  1.18  1.12  1.08  1.05  1.04  1.05  1.05  1.06    1.44    1.20    1.05      1.05
2021年  1.10  1.10  1.13  1.14  1.15  1.15  1.16  1.17  1.17    1.09    1.11    1.15      1.17
2022年  1.22  1.24   NaN   NaN   NaN   NaN   NaN   NaN   NaN    1.21     NaN     NaN       NaN
```

`s_jobs.index`の`list`を取得。

``` Python 3.10
>>> list(s_jobs.index)[:12]
[('1963年', '１月'), ('1963年', '２月'), ('1963年', '３月'), ('1963年', '４月'), ('1963年', '５月'), ('1963年', '６月'), ('1963年', '７月'), ('1963年', '８月'), ('1963年', '９月'), ('1963年', '10月'), ('1963年', '11月'), ('1963年', '12月')]
```

`index`を日付に変換する関数

``` Python 3.10
>>> def parse_year_and_month(year, month):
...     year = int(year[:-1])
...     month = int(month[:-1])
...     year += (1900 if year >= 63 else 2000)
...     return datetime(year, month, 1)
...
>>> parse_year_and_month("63年", "1月")
datetime.datetime(1963, 1, 1, 0, 0)
>>> parse_year_and_month("3年", "1月")
datetime.datetime(2003, 1, 1, 0, 0)
>>> parse_year_and_month("４３年", "1月")
datetime.datetime(2043, 1, 1, 0, 0)
```

``` Python 3.10
>>> s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]
>>> s_jobs
3863-01-01 00:00:00    0.56
3863-02-01 00:00:00    0.60
3863-03-01 00:00:00    0.64
3863-04-01 00:00:00    0.68
3863-05-01 00:00:00    0.71
                       ...
3922-01-01 00:00:00    1.20
3922-02-01 00:00:00    1.21
3922-03-01 00:00:00    1.22
3922-04-01 00:00:00    1.23
3922-05-01 00:00:00    1.24
Length: 713, dtype: float64
```

</details>

<details>
<summary>read_html</summary>

``` Python 3.10
>>> dfs = pd.read_html("https://www.python.org/dev/peps/") 
>>> len(dfs)
12
>>> dfs[1]
   Unnamed: 0   PEP                                              Title                                            Authors
0           I    13                         Python Language Governance                                         python-dev
1           I    20                                  The Zen of Python                                             Peters
2           I   101                          Doing Python Releases 101                                        Warsaw, GvR
3          IF   247               API for Cryptographic Hash Functions                                           Kuchling
4          IF   248             Python Database API Specification v1.0                                            Lemburg
5          IF   249             Python Database API Specification v2.0                                            Lemburg
6           I   257                              Docstring Conventions                                       Goodger, GvR
7          IF   272           API for Block Encryption Algorithms v1.0                                           Kuchling
8           I   287                  reStructuredText Docstring Format                                            Goodger
9           I   290                   Code Migration and Modernization                                          Hettinger
10         IF   291  Backward Compatibility for the Python 2 Standa...                                            Norwitz
11         IF   333           Python Web Server Gateway Interface v1.0                                                Eby
12          I   394          The “python” Command on Unix-Like Systems  Staley, Coghlan, Warsaw, Viktorin, Hrončok, Wi...
13         IF   399  Pure Python/C Accelerator Module Compatibility...                                             Cannon
14         IF   404                     Python 2.8 Un-release Schedule                                             Warsaw
15          I   411  Provisional packages in the Python standard li...                                 Coghlan, Bendersky
16         IF   430  Migrating to Python 3 as the default online do...                                            Coghlan
17          I   434        IDLE Enhancement Exception for All Branches                                      Rovito, Reedy
18         IF   452          API for Cryptographic Hash Functions v2.0                                   Kuchling, Heimes
19         IF   457            Notation For Positional-Only Parameters                                           Hastings
20          I   478                        Python 3.5 Release Schedule                                           Hastings
21         IF   482                 Literature Overview for Type Hints                                              Langa
22         IF   483                           The Theory of Type Hints                                    GvR, Levkivskyi
23          I   514        Python registration in the Windows registry                                              Dower
24          I   537                        Python 3.7 Release Schedule                                              Deily
25          I   569                        Python 3.8 Release Schedule                                              Langa
26         IF   579                Refactoring C functions and methods                                            Demeyer
27          I   596                        Python 3.9 Release Schedule                                              Langa
28         IA   602                    Annual Release Cycle for Python                                              Langa
29         IF   607        Reducing CPython’s Feature Delivery Latency                              Langa, Dower, Coghlan
30          I   630                        Isolating Extension Modules                                           Viktorin
31         IF   635  Structural Pattern Matching: Motivation and Ra...                                          Kohn, GvR
32         IF   636              Structural Pattern Matching: Tutorial                                            Moisset
33         IA   668  Marking Python base environments as “externall...  Thomas, Klose, Laíns, Stufft, Chung, Rivera, H...
34          I   672  Unicode-related Security Considerations for Py...                                           Viktorin
35          I   801                                           Reserved                                             Warsaw
36         IF  3333         Python Web Server Gateway Interface v1.0.1                                                Eby
37          I  8000       Python Language Governance Proposal Overview                                             Warsaw
38          I  8002                      Open Source Governance Survey           Warsaw, Langa, Pitrou, Hellmann, Willing
39         IA  8016                         The Steering Council Model                                      Smith, Stufft
40          I  8100             January 2019 steering council election                                      Smith, Durbin
41          I  8101                2020 Term steering council election                                  Jodlowska, Durbin
42          I  8102                2021 Term steering council election                           Jodlowska, Durbin, Carey
43          I  8103                2022 Term steering council election                           Jodlowska, Durbin, Carey
```

</details>

## Matplotlib

<details>
<summary>基本的な使い方</summary>

`pip install`

``` PowerShell
(venv)pip install matplotlib japanize-matplotlib
```

``` Python 3.10
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib.pyplot as plt
>>> import japanize_matplotlib
>>> x = [i for i in range(1,6)]
>>> y = [ i * 3 + 1 for i in range(len(x))]
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x00000184AF6F0A30>]
>>> plt.show()
# dpiは画角を指定する。dpi=100では1px=1mmとなる。
# show()を実行した後にsavefig()を実行すると、真っ白な画像が生成されてしまう。
>>> plt.savefig("white.png", dpi=500)
# 事前にimage保存用のフォルダを作成しておく
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x00000184AD833820>]
>>> plt.savefig("graph_images/graph.png", dpi=500)
```

</details>

<details>
<summary>matplotlib.pyplotにseabornのスタイルを適用する</summary>

``` Python 3.10
`linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'`
```

</details>

