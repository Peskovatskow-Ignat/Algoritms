"""
Сложность алгоритма в худшем случае составляет O(n)
n - количество элементов в списке prices
в худшем случае мы пройдемся по всем элементам списка два раза.
"""

def getDescentPeriods(prices):
    n = len(prices)
    smooth_periods = n  # каждый элемент массива - период плавного спуска длины 1

    # проходимся по массиву цен
    for i in range(1, n):
        j = i
        # ищем все последовательные дни с плавным спуском цены
        while j < n and prices[j] == prices[j-1]-1:
            j += 1
        # добавляем количество периодов плавного спуска, найденных на текущей итерации
        smooth_periods += j-i

    # учитываем еще один период плавного спуска длины 1 - последний элемент массива
    return smooth_periods

def foo(price):
    dp = [1] * len(price)
    s = 1
    for i in range(1, len(price)):
        if price[i - 1] - 1 == price[i]:
            dp[i] = dp[i - 1] + 1
        s += dp[i]
    return s