import sys
from pathlib import Path
import argparse

current_dir = Path(__file__).resolve().parent
src_dir = current_dir.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))
from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортировка пар (word, count)"""
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))

def main():
    parser = argparse.ArgumentParser(description="Генерация частотного отчёта")
    parser.add_argument("--in", default="data/lab04/input.txt", dest="input_file")
    parser.add_argument("--out", default="data/lab04/report.csv", dest="output_file")
    parser.add_argument("--encoding", default="utf-8") # <-- сюда передастся cp1251
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    text = read_text(input_path, encoding=args.encoding)
   
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    sorted_rows = sorted_word_counts(freq)

    header = ("word", "count")
    write_csv(sorted_rows, output_path, header=header)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")
if __name__ == "__main__":
    main()