'''
Сложность: О(n)
Алгоритм принимает на вход целое число
Если число чётное делит его на 2
Если нечётное вычитает из него единицу
Считает количество итераций
'''


def numberOfSteps(num):
    k = 0  # Вводим переменную счётчик
    while num > 0:  # Проверяем когда закончится наш алгоритм
        if num % 2 == 0:  # Проверка на чётность
            num /= 2  # Деление на 2
            k += 1  # Добавялем к количеству итераций единицу
        else:  # Если нечётное
            num -= 1  # Вычитем единицу
            k += 1  # Добавялем к количеству итераций единицу
    return k  # Возращаем коичество итераций

print(numberOfSteps(12345))
