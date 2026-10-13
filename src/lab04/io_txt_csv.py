from pathlib import Path
import csv
from typing import Iterable, Sequence, Union

def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """Читает текст из файла целиком."""
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(
    rows: Iterable[Sequence],
    path: Union[str, Path],
    header: tuple[str, ...] | None = None
) -> None:
    """Записывает строки в CSV-файл с помощью модуля csv и newline=""."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)