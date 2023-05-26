"""
Сложность данного алгоритма - O(n), где n - индекс.
"""

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1  # a, b, c - значениями первых трех элементов последовательности
    curr = 3  # текущий индекс - 3

    while curr <= n:  # Цикл выполняется до достижения текущего индекса значения n
        a, b, c = b, c, a + b + c  # Обновляем значения переменных a, b, c
