# ЛР2, Задание B — matrix.py


def transpose(mat: list[list[float | int]]) -> list[list]:
    """Поменять строки и столбцы местами."""
    if not mat:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")
    res = []
    for j in range(cols):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        res.append(new_row)
    return res


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке."""
    if not mat:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")
    res = []
    for row in mat:
        res.append(sum(row))
    return res


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу."""
    if not mat:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")
    res = []
    for j in range(cols):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res


# transpose
print(transpose([[1, 2, 3]]))       # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))   # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([]))                # []

# row_sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))   # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))     # [0, 0]
print(row_sums([[0, 0], [0, 0]]))         # [0, 0]

# col_sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))   # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))     # [9, -9]
print(col_sums([[0, 0], [0, 0]]))         # [0, 0]

# кейсы с ошибками
try:
    print(transpose([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)

try:
    print(row_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)

try:
    print(col_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)