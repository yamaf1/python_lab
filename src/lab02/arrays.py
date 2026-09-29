def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимум и максимум списка"""
    if not nums:
        raise ValueError("Список пуст")
    mn = nums[0]
    mx = nums[0]
    for item in nums:
        if item < mn:
            mn = item
        if item > mx:
            mx = item
    return (mn, mx)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает уникальные значения по возрастанию"""
    lst = []
    for item in nums:
        if item not in lst:
            lst.append(item)
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def flatten(mat: list[list | tuple]) -> list:
    """Разворачивает матрицу в один список"""
    lst = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент не является строкой матрицы")
        for i in row:
            lst.append(i)
    return lst



print(min_max([3, -1, 5, 5, 0]))    
print(min_max([42]))                
print(min_max([-5, -2, -9]))        
try:
    print(min_max([]))
except ValueError as e:
    print("ValueError:", e)
print(min_max([1.5, 2, 2.0, -3.1])) 

print(unique_sorted([3, 1, 2, 1, 3]))       
print(unique_sorted([]))                    
print(unique_sorted([-1, -1, 0, 2, 2]))     
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 

print(flatten([[1, 2], [3, 4]]))    
print(flatten([[1, 2], (3, 4, 5)])) 
print(flatten([[1], [], [2, 3]]))   
try:
    print(flatten([[1, 2], "ab"]))
except TypeError as e:
    print("TypeError:", e)