#!/bin/bash/env python3

import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.co.jp/")
print(browser.url)


browser.select_form('form[action="/search"]')
browser["q"] = "MechanicalSoup"
browser.submit_selected()
page = browser.get_current_page()
# print(page)

for a in page.select("a:has(h3)"):
    text = a.text
    url = browser.absolute_url(a.get("href"))
    print(f"text: {text} url: {url}")
