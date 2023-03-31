"""
Сложность данного алгоритма - O(rows * cols)
"""

def islandPerimeter(grid):
    # Получаем размеры сетки
    x = len(grid)
    y = len(grid[0])

    # Инициализируем счетчик периметра
    perimeter = 0

    # Перебираем каждую клетку в сетке
    for i in range(x):
        for j in range(y):
            # Проверяем, является ли клетка землей
            if grid[i][j] == 1:
                # Проверяем соседей клетки
                if i == 0 or grid[i-1][j] == 0: # сверху
                    perimeter += 1
                if i == x - 1 or grid[i+1][j] == 0: # снизу
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0: # слева
                    perimeter += 1
                if j == y - 1 or grid[i][j+1] == 0: # справа
                    perimeter += 1

    # Возвращаем счетчик периметра
    return perimeter
