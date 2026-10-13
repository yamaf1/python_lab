# python_lab

# Лабораторная работа 3 — Тексты и частоты слов (словарь/множество)
## Задание A

## `normalize`

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Функция приводит текст к единому регистру и убирает пробелы."""
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = re.sub(r"\s+", " ", text)
    return text.strip()
```
Функция приводит строку к нужному регистру, заменяет «ё» на «е» и удаляет лишние пробелы.

![функция 1](../../images/lab03/image1.1.png)

## `tokenize`
```python
def tokenize(text: str) -> list[str]:
    """Функция считывает из текста слова, включая слова с дефисом и числа."""
    return re.findall(r"\w+(?:-\w+)*", text)
```

Функция разбивает строку на список отдельных слов с учётом слов с дефисом и чисел.

![функция 2](../../images/lab03/image1.2.png)

## `count_freq и top_n`
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    """Функция возвращает словарь с количеством каждого слова."""
    freq: dict[str, int] = {}
    for w in tokens:
        freq[w] = freq.get(w, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Функция возвращает n самых частых слов."""
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

Функция count_freq считает частоту вхождения каждого слова из списка и возвращает словарь.

Функция top_n возвращает список из 5 самых частых слов, отсортированных по убыванию частоты и алфавиту.
![функция 3 4](../../images/lab03/image1.3.png)

## Задание В

```python
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from lib.text import count_freq, normalize, tokenize, top_n


def main():
    sys.stdin.reconfigure(encoding='utf-8')
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
```

Обрабатывает текст с помощью функций библиотеки lib.text и выводит в консоль статистику: общее число слов, количество уникальных слов и топ-5 самых частых слов.
![функция 5](../../images/lab03/image2.png)