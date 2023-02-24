"""
Сложность данного алгоритма составляет O(n)
n - входной параметр функции.
"""

def get_maximum_generated(n):
    if n == 0:
        return 0  # Если n = 0, то вернуть 0, так как массив nums будет пустым

    nums = [0] * (n + 1)  # Создаем массив nums, заполненный нулями
    nums[1] = 1  # Инициализируем nums[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:  # Если i четное, то nums[i] = nums[i // 2]
            nums[i] = nums[i // 2]
        else:  # Иначе i нечетное и nums[i] = nums[i // 2] + nums[i // 2 + 1]
            nums[i] = nums[i // 2] + nums[i // 2 + 1]

    return max(nums)  # Возвращаем максимальное значение в массиве nums