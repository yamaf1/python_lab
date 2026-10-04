# python_lab

# Лабораторная работа 2
## Задание 1

## `min_max`

![min_max](../../images/lab02/image1.1.png)

Программа возвращает кортеж из минимума и максимума списка.

---

## `unique_sorted`

![unique_sorted](../../images/lab02/image1.2.png)

Программа выводит новый список из уникальных значений исходного, отсортированный по возрастанию.

---

## `flatten`

![flatten](../../images/lab02/image1.3.png)

Программа превращает список кортежей в один плоский список по строкам.

## Задание 2

## `transpose`

![transpose](../../images/lab02/image2.1.png)

Функция меняет строки и столбцы местами.

---

## `row_sums`

![row_sums](../../images/lab02/image2.2.png)

Функция выводит сумму по каждой строке.

---

## `col_sums`

![col_sums](../../images/lab02/image2.3.png)

Функция выводит сумму по каждому столбцу.

## Задание 3

## `format_record`
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("В записи должно быть 3 элемента")
    fio, group, gpa = rec
    if type(fio) != str or type(group) != str:
        raise TypeError("ФИО и группа должны быть строками")
    if type(gpa) != int and type(gpa) != float:
        raise TypeError("GPA должен быть числом")
    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not (0 <= gpa <= 5):
        raise ValueError("GPA должен быть от 0 до 5")
    if len(fio.split()) != 2 and len(fio.split()) != 3:
        raise ValueError("Неверное ФИО")
    parts = fio.split()
    for p in parts:
        if not p.replace("-", "").isalpha():
            raise ValueError("ФИО должно состоять только из букв")
    surname = parts[0].capitalize()
    group = group.strip()
    initials = ""
    for p in parts[1:]:
        initials += p[0].upper() + "."
    return f"\"{surname} {initials}, гр. {group}, GPA {gpa:.2f}\""
```

![tuples](../../images/lab02/image3.png)

Программа получает строку, убирает лишние пробелы, приводит к нужному виду и выводит.