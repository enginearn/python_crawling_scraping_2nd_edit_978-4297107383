from base64 import encode
import csv
from chardet import detect

file_name = "top_cities.csv"
encoding = detect(open(file_name, "rb").read())["encoding"]
print(f"encoding: {encoding}")

with open(file_name, "w", encoding=encoding, newline="") as f:
    writer = csv.DictWriter(f, ["rank", "city", "population"])
    writer.writeheader() # header出力
    writer.writerows([
        {"rank": 1, "city": "上海", "population": 24150000},
        {"rank": 2, "city": "カラチ", "population": 23500000},
        {"rank": 3, "city": "北京", "population": 21516000},
        {"rank": 4, "city": "天津", "population": 14722100},
        {"rank": 5, "city": "イスタンブール", "population": 14160467},
    ])