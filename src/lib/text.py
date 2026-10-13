import re


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


def tokenize(text: str) -> list[str]:
    """Функция считывает из текста слова, включая слова с дефисом и числа."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Функция возвращает словарь с количеством каждого слова."""
    freq: dict[str, int] = {}
    for w in tokens:
        freq[w] = freq.get(w, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Функция возвращает 5 самых частых слов."""
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

if __name__ == "__main__":
    print("--- normalize ---")
    print(f'"ПрИвЕт\\nМИр\\t" -> "{normalize("ПрИвЕт\nМИр\t")}"')
    print(f'"ёжик, Ёлка" -> "{normalize("ёжик, Ёлка")}"')
    print(f'"Hello\\r\\nWorld" -> "{normalize("Hello\r\nWorld")}"')
    print(f'"  двойные   пробелы  " -> "{normalize("  двойные   пробелы  ")}"')

    print("\n--- tokenize ---")
    print(f'"привет мир" -> {tokenize("привет мир")}')
    print(f'"hello,world!!!" -> {tokenize("hello,world!!!")}')
    print(f'"по-настоящему круто" -> {tokenize("по-настоящему круто")}')
    print(f'"2025 год" -> {tokenize("2025 год")}')
    print(f'"emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}')

    print("\n--- Тесты count_freq и top_n ---")
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    print(f"Токены {tokens1} -> частоты {freq1}")
    print(f"top_n(..., n=2) -> {top_n(freq1, n=2)}")

    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    freq2 = count_freq(tokens2)
    print(f"Тай-брейк {tokens2} -> частоты {freq2}")
    print(f"top_n(..., n=2) -> {top_n(freq2, n=2)}")