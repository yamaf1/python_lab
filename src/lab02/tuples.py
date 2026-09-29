def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    parts = fio.split()
    surname = parts[0].capitalize()
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