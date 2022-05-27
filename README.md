# Python クローリング＆スクレイピング

##　UNIXコマンドでのスクレイピング

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

``` 
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
  File "C:\Users\nagar\Development\Python\crawling_scraping_2nd_edit\venv\lib\site-packages\requests\models.py", line 910, in json
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
  File "C:\Users\nagar\Development\Python\crawling_scraping_2nd_edit\venv\lib\site-packages\requests\models.py", line 917, in json
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

## BeatifulSoup4

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
