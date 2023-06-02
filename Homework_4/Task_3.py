"""
Сложность данного алгоритма - O(n), где n - кол-во чиссел.
"""

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    first, second, three = 0, 1, 1  # значениями первых трех элементов последовательности
    curr = 3  # текущий индекс - 3

    while curr <= n:  # Цикл выполняется до достижения текущего индекса значения n
        first, second, three = second, three, first + second + three  # Обновляем значения переменных
        curr +=1
    answer = three 
    return answer
