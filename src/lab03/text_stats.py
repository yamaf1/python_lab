import os
import sys

# Добавляем корневую директорию src в sys.path для импорта модуля lib
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from lib.text import count_freq, normalize, tokenize, top_n


def main():
    text = sys.stdin.read()
    if not text:
        return
    
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top5 = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()