#

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
