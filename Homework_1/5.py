'''
Сложность: О(n)
Алгоритм ищет последовательность открывающихся и закрывающихся скобок в скобках
'''


def removeOuterParentheses(s):
    list_1 = ''  # Создаём строку для записи последовательности открытых и закрытых скобок
    count = 1  # Для счёта последовательности
    i = 1  # Для прохода по строке
    while i < len(s):
        if s[i] == '(':  # Если скобка открывающая то сount обозначает незаконченную последовательность скобок
            count += 1
        elif s[i] == ')':  # Если скобка акрывающая то сount обозначает законченную последовательность скобок
            count -= 1
        if count == 0:  # Если последовательнось скобок закрывается переходим на новый блок
            # print(i, s[i], s[i-1])
            i += 2
            count += 1
            continue  # Игнорируем то что написано ниже в цикли и начинаем проверку цикла заново.
        list_1 += s[i]  # Записывааем символы в строку
        i += 1  # Переход на следующий символ
    return list_1  # Возвращаем ответ

print(removeOuterParentheses('()(()())(())'))



