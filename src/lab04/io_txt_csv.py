from pathlib import Path
import csv
from typing import Iterable, Sequence

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(
        rows: Iterable[Sequence],
        path: str | Path,
        header: tuple[str, ...] | None = None
) -> None:
    """Создаёт или перезаписывает CSV-файл с разделителем ','."""
    p = Path(path)
    ensure_parent_dir(p)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)