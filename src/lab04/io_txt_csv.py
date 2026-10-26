from pathlib import Path
import csv
from typing import Iterable, Sequence

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """ Открывает файл и читает в заданной кодировке.

    По умолчанию кодировка UTF-8. Для другой кодировки укажите encoding,
    например: read_text("data/lab04/input.txt", encoding="cp1251").

    Raises:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если файл нельзя прочитать в этой кодировке.
    """
    p = Path(path)
    return Path(path).read_text(encoding=encoding)

def write_csv(
        rows: Iterable[Sequence],
        path: str | Path,
        header: tuple[str, ...] | None = None
) -> None:
    """Создаёт или перезаписывает CSV-файл"""
    p = Path(path)
    ensure_parent_dir(p)
    rows = list(rows)
    if rows:
        etalon = len(rows[0])
        for r in rows:
            if len(r) != etalon:
                raise ValueError('Строки разной длинны')

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)