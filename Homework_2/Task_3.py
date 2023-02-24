"""
Сложность данного алгоритма составляет O(mn)
m - количество строк в сетке
n - количество столбцов.
"""


def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])  # Получаем размеры сетки
    dp = [[0 for _ in range(n)] for _ in range(m)]  # Инициализируем матрицу dp
    print(dp)
    
    # Заполняем первый столбец матрицы dp
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    
    # Заполняем первую строку матрицы dp
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1
    
    # Заполняем оставшуюся часть матрицы dp
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:  # Если нет препятствия
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Обновляем значение в матрице dp
    
    return dp[m-1][n-1]  # Возвращаем количество уникальных путей до последней клетки сетки
