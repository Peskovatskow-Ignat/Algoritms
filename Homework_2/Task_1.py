"""
Сложность данного алгоритма составляет O(m*n)
m - количество строк
n - количество столбцов.
"""

def countSquares(matrix):
    m, n = len(matrix), len(matrix[0]) # Получаем размеры матрицы
    count = 0 # Инициализируем счетчик

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and i > 0 and j > 0: # Если элемент не находится в первой строке или первом столбце
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
            count += matrix[i][j] # Добавляем текущий элемент в счетчик

    return count