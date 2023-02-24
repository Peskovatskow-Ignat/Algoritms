"""
Сложность данного алгоритма составляет O(n)
n - длина списка nums.
"""

def rob(nums):  # Обработка особых случаев, если длина списка nums равна 0, 1 или 2.
    n = len(nums)
    if n == 0:  # если nums пустой список
        return 0
    if n == 1:  # если в nums только один дом
        return nums[0]
    if n == 2:  # если в nums два дома
        return max(nums[0], nums[1])
    
    
# Функция для вычисления максимальной прибыли в интервале [start, end]
    def rob_helper(start, end):
        # Инициализация переменных prev1 и prev2 для хранения максимальной прибыли двух предыдущих домов
        prev1, prev2 = 0, 0
        # Проходимся циклом по домам от start до end и вычисляем максимальную прибыль, которую можно получить
        for i in range(start, end):
            # Вычисляем текущую максимальную прибыль, которую можно получить при учете i-го дома
            curr_max = max(prev1, prev2 + nums[i])
            # Обновляем значения prev1 и prev2 для следующей итерации
            prev2 = prev1
            prev1 = curr_max

        return curr_max # Возвращаем максимальную прибыль, которую можно получить в интервале [start, end]

    # Возвращаем максимум из двух значений: максимальная прибыль при рассмотрении домов с 0 до n-2 
    # А так же максимальную прибыль при рассмотрении домов с 1 до n-1 
    return max(rob_helper(0, n - 1), rob_helper(1, n))

