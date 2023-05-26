"""
сложность алгоритма - O(log n), где n - кол-вo элементов в массиве.
"""

def twoCitySchedCost(costs):
    totalCost = 0
    costs.sort(key=lambda x: x[0] - x[1])  # Сортируем массив costs на основе разницы между стоимостью отправки человека в город A и отправки человека в город B
    n = len(costs) // 2  # Вычисляем количество людей, которых следует отправить в каждый город
    
    for i in range(n):
        totalCost += costs[i][0]  # Добавляем стоимость отправки человека в город A к totalCost
        
    for i in range(n, len(costs)):
        totalCost += costs[i][1]  # Добавляем стоимость отправки человека в город B к totalCost
    
    return totalCost
