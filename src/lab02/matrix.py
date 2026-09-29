def transpose(mat: list[list[float | int]]) -> list[list]:
    """Транспонирует матрицу: строки в столбцы"""
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
    """Возвращает сумму по каждой строке матрицы"""
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
    """Возвращает сумму по каждой строке матрицы"""
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

print(transpose([[1, 2, 3]]))       
print(transpose([[1], [2], [3]]))   
print(transpose([[1, 2], [3, 4]]))  
print(transpose([]))                
try:
    print(transpose([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)

print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))     
print(row_sums([[0, 0], [0, 0]]))        
try:
    print(row_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)

print(col_sums([[1, 2, 3], [4, 5, 6]]))   
print(col_sums([[-1, 1], [10, -10]]))     
print(col_sums([[0, 0], [0, 0]]))        
try:
    print(col_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)