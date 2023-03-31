"""
сложность O(n), где n - это количество узлов в связанном списке
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Создаем указатель ptr и присваиваем ему начальное значение head
        ptr = head
        # Создаем пустую строку для хранения двоичной строки
        s = ''
        # Пока указатель не равен None
        while ptr != None:
            # Преобразуем значение узла в строку и добавляем его к строке s
            s += str(ptr.val) 
            # Переходим к следующему узлу списка
            ptr = ptr.next
        # Преобразуем двоичную строку в десятичное число и возвращаем его
        return int(s, 2)
