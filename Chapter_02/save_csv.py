import csv

csv_file = "top_cities.csv"

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["rank", "city", "population"])
    writer.writerows([
        [1, "上海", 24150000],
        [2, "カラチ", 23500000],
        [3, "北京", 21516000],
        [4, "天津", 14722100],
        [5, "イスタンブール", 14160467],
    ])