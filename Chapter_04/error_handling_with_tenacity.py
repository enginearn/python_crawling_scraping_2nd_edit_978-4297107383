from urllib import response
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)

@retry(stop=stop_after_attempt(3),
wait=wait_exponential(multiplier=1))
def fetch(url: str) -> requests.Response:
    """指定したURLにリクエストを送り、Responseオブジェクトを返す
    一時的なエラーが起きた場合は最大3回リトライする
    3回リトライしても成功しなかった場合は例外Exceptionを発生させる
    """
    print(f"Retrieving: {url}")
    response = requests.get(url)
    if response.status_code not in TEMPORARY_ERROR_CODES:
        return response

    raise Exception(f"Temporary Error: {response.status_code}")

def main():
    """メインとなる処理
    """
    response = fetch("http://httpbin.org/status/200,404,503")
    if 200 <= response.status_code < 300:
        print("Success!")
    else:
        print("Error!")

if __name__ == "__main__":
    main()