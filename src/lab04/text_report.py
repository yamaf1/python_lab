import sys
from pathlib import Path

# Добавляем путь к src, чтобы Python видел lib и lab04
current_dir = Path(__file__).resolve().parent
src_dir = current_dir.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

# Импортируем готовые функции из твоей библиотеки (ЛР3) и модуля ввода-вывода
from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import write_csv


def main():
    input_path = Path("data/lab04/input.txt")
    output_path = Path("data/lab04/report.csv")

    # 1. Чтение файла с защитой: используем with и ловим FileNotFoundError (из лекции)
    try:
        with open(input_path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ошибка: файл не найден: {input_path}", file=sys.stderr)
        sys.exit(1)

    # 2. Конвейер обработки текста с использованием твоих функций из ЛР3
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)

    # 3. Сортировка для CSV-отчёта: берём всю базу frequency.items() 
    # и сортируем по правилу ТЗ (сначала частота ↓, затем слово ↑), 
    # аналогично тому, как это сделано внутри твоего top_n
    sorted_rows = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # 4. Запись отчёта в CSV
    header = ("word", "count")
    write_csv(sorted_rows, output_path, header=header)

    # 5. Вывод краткой сводки в консоль (с использованием твоей функции top_n)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-5 слов: {top_n(freq, 5)}")
    print(f"Отчёт успешно сохранен в {output_path}")


if __name__ == "__main__":
    main()