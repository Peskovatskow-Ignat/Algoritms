"""
сложность O(n), где n - это количество элементов в связном списке
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:        
# Создаем пустой список для хранения значений в связанном списке
    vals = []

    # Пока head не равно None, добавляем значения в список vals и перемещаемся по списку
    while head:
        vals.append(head.val)
        head = head.next

    # Сравниваем список со своим перевернутым эквивалентом и возвращаем результат сравнения
    return vals == vals[::-1]


