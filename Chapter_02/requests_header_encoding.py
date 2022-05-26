# import io
import sys
import requests

url = sys.argv[1]
r = requests.get(url)
print(f"encoding: {r.encoding}", file=sys.stderr)

# Linux, Mac, 
# Window10でシステムロケールのベータ: ワールドワイド言語サポートで、
# Unicode UTF-8にチェックを入れている場合
print(r.text)

# Windows
# python script_name.py https://sample.com > index.htmlで
# リダイレクトファイル出力できない...
# html =r.text.encode("utf-8", errors="ignore")
# html = html.decode("utf-8_sig", errors="ignore")
# print(html, file=sys.stderr)
