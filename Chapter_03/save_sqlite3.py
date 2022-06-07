from logging import PlaceHolder
import sqlite3

conn = sqlite3.connect("top_cities.db")

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS cities")
c.execute("""
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
""")

# リストの場合、パラメーターで置き換える場所(PlaceHolder)は ? で指定する
c.execute("INSERT INTO cities VALUES (?, ?, ?)", (1, "上海", 24150000))

# パラメーターが辞書の場合、placeholderは : キー名 で指定する
c.execute("INSERT INTO cities VALUES (:rank, :city, :population)", 
            {"rank": 2, "city": "カラチ", "population": 23500000})

# executemany()で、複数のパラメーターをリストで指定できる
c.executemany("INSERT INTO cities VALUES (:rank, :city, :population)", 
[
    {"rank": 3, "city": "北京", "population": 21516000},
    {"rank": 4, "city": "天津", "population": 1472210},
    {"rank": 5, "city": "イスタンブール", "population": 14160467},
])

conn. commit()

c.execute("SELECT * FROM cities")
for row in c.fetchall():
    print(row)

conn.close()
