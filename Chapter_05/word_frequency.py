import sys
import os
from glob import glob
from typing import List, Iterator, TextIO
from collections import Counter

import MeCab


def iter_doc_contents(file: TextIO) -> Iterator[str]:
    """ファイルオブジェクトを読み込んで、記事の中身(開始タグ<doc ...>と終了タグ</doc>の間のテキスト)を
    順に返すジェネレーター関数
    """
    for line in file:
        if line.startswith("<doc "):
            buffer = []
        elif line.startswith("</doc>"):
            content = "".join(buffer)
            yield content
        else:
            buffer.append(line)

def get_words(tagger: str, content: str) -> List[str]:
    """文字列内に出現する名詞のリスト(重複含む)を取得する関数
    """
    words = []
    node = tagger.parseToNode(content)
    while node:
        pos, pos_sub1 = node.feature.split(",")[:2]
        if pos == "名詞" and pos_sub1 in ("固有名詞", "一般"):
            words.append(node.surface)
        node = node.next

    return words

def main():
    """コマンドライン引数で指定したディレクトリ内の
    ファイルを読み込んで非出単語を表示する
    """
    input_dir = sys.argv[1] # python .\word_frequency.py .\articles\

    tagger = MeCab.Tagger("")
    tagger.parse("")

    frequency = Counter()
    count_proccessed = 0

    for path in glob(os.path.join(input_dir, '*', 'wiki_*')):
        print(f"Processing {path}...", file=sys.stderr)

        with open(path) as file:
            for content in iter_doc_contents(file):
                tokens = get_words(tagger, content)
                frequency.update(tokens)

                count_proccessed += 1
                if count_proccessed % 10000 == 0:
                    print(f"{count_proccessed} documents were processed.",
                    file=sys.stderr)

    for word, count in frequency.most_common(30):
        print(word, count)

if __name__ == "__main__":
    main()
