from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv

# 1. Пустой файл -> пустая строка
Path("data/lab04/empty.txt").write_text("", encoding="utf-8")
txt = read_text("data/lab04/empty.txt")
print("1. Пустой файл:", repr(txt))

# 2. Пустой rows, без заголовка -> пустой файл
write_csv([], "data/lab04/empty.csv")
txt_1 = read_text("data/lab04/empty.csv")
print("2. Пустой rows без header:", repr(txt_1))

# 3. Пустой rows с заголовком -> только заголовок
write_csv([], "data/lab04/header_only.csv", header=("a", "b"))
txt_2 = read_text("data/lab04/header_only.csv").splitlines()
print("3. Пустой rows с header:", txt_2)

# 4. Файл не существует -> FileNotFoundError
try:
    read_text("data/lab04/no_such_file.txt")
except FileNotFoundError:
    print("4. Файла нет -> FileNotFoundError")

# 5. Неподходящая кодировка -> UnicodeDecodeError
Path("data/lab04/win1251.txt").write_text("Привет", encoding="cp1251")
try:
    read_text("data/lab04/win1251.txt")
except UnicodeDecodeError:
    print("5. Файл в cp1251, читаем как utf-8 -> UnicodeDecodeError")

# 6. Строки разной длины -> ValueError
try:
    write_csv([("a", 1), ("b",)], "data/lab04/bad.csv")
    print("6. Ошибка не возникла (а должна была)")
except ValueError:
    print("6. Строки разной длины -> ValueError")
