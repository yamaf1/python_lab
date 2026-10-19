from src.lab04.io_txt_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt", encoding="cp1251")  # должен вернуть строку
print("Прочитано:", repr(txt))
print("Тип:", type(txt))

write_csv([("word", "count"), ("test", 3)], "data/check.csv")  # создаст CSV
print("CSV создан: data/check.csv")