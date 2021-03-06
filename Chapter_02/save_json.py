import json

file_name = "top_cities.json"
encoding = "utf-8"

cities = [
    {"rank": 1, "city": "上海", "population": 24150000},
    {"rank": 2, "city": "カラチ", "population": 23500000},
    {"rank": 3, "city": "北京", "population": 21516000},
    {"rank": 4, "city": "天津", "population": 14722100},
    {"rank": 5, "city": "イスタンブール", "population": 14160467},
]

print(json.dumps(cities, ensure_ascii=False, indent=2))

with open(file_name, "w", encoding=encoding) as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)
    print("done!")