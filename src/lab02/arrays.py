def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимум и максимум списка"""
    if not nums:
        raise ValueError("Список пуст")
    low = nums[0]
    high = nums[0]
    for item in nums:
        if item < low:
            low = item
        if item > high:
            high = item
    return (low, high)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает уникальные значения по возрастанию"""
    uniq = []
    for item in nums:
        if item not in uniq:
            uniq.append(item)
    for i in range(len(uniq)):
        for j in range(len(uniq) - 1 - i):
            if uniq[j] > uniq[j + 1]:
                uniq[j], uniq[j + 1] = uniq[j + 1], uniq[j]
    return uniq


def flatten(mat: list[list | tuple]) -> list:
    """Разворачивает матрицу в один список"""
    flat = []
    for chunk in mat:
        if not isinstance(chunk, (list, tuple)):
            raise TypeError("Элемент не является строкой матрицы")
        for cell in chunk:
            flat.append(cell)
    return flat



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