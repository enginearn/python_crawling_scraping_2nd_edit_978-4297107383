import sys
import logging
from collections import Counter
from pathlib import Path
from typing import List, Iterator, TextIO

import MeCab

tagger = MeCab.Tagger("")
tagger.parse("")

def count_words(file: TextIO) -> Counter:
    """WikiExtractorが出力したファイルに含まれる
    全ての記事から単語の出現頻度を数える関数
    """
    frequency = Counter()
    num_docs = 0

    for content in iter_doc_contents(file):
        words = get_words(content)
        frequency.update(words)
        num_docs += 1
        logging.info(f"Found {len(frequency)} words from {num_docs} documents")

        return frequency

def iter_doc_contents(file: TextIO) -> Iterator[str]:
    """ファイルオブジェクトを読み込んで、記事の中身(開始タグ<doc ...>と終了タグ</doc>の間のテキスト)を
    順に返すジェネレーター関数
    """
    for line in file:
        if line.startswith("<doc "):
            buffer = []
        elif line.startswith("</doc>"):
            content = " ".join(buffer)
            yield content
        else:
            buffer.append(line)

def get_words(content: str) -> List[str]:
    """文字列内に出現する名詞のリスト(重複含む)を取得する関数
    """
    words = []
    node = tagger.parseToNode(content)
    while node:
        pos, pos_sub1 = node.feature.split(",")[:2]
        if pos == "名詞" and pos_sub1 in ("固有名詞", "一般"):
            words.append(node.surface)
        node.next

    return words

def main():
    """コマンドライン引数で指定したディレクトリ内の
    ファイルを読み込んで非出単語を表示する
    """

    input_dir = Path(sys.argv[1])
    frequency = Counter()

    for path in sorted(input_dir.glob("*/wiki_*")):
        logging.info(f"Processing {path}...")

        with open(path) as file:
            frequency += count_words(file)

    for word, count in frequency.most_common(30):
        print(word, count)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()