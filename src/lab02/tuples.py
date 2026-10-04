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

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

try:
    print(format_record(("", "BIVT-25", 4.6)))
except ValueError as e:
    print("ValueError:", e)

try:
    print(format_record(("Иванов Иван", "", 4.6)))
except ValueError as e:
    print("ValueError:", e)

try:
    print(format_record(("Иванов Иван", "BIVT-25", "4.6")))
except TypeError as e:
    print("TypeError:", e)