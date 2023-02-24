'''
Cложность: O(n)
Алгорим принимает на вход 2 стоки
Ищет подстроку в другой строке
'''

def numJewelsInStones(jewels, stones):
    count = 0  # Переменная счётчик
    for i in stones:  # Проходим по строке
        if i in jewels: # Пррверяем есть ли подстрока в строке
            count += 1  # Если есть к счётчику добавляем 1
    return count  # Возвращаем ответ


print(numJewelsInStones('zZ', 'zZzZzzZzzzn'))