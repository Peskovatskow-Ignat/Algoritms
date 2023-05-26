"""
сложность алгоритма - O(H), где H - высота дерева.
"""

class Solution(object):
    def getMinimumDifference(self, root):
        self.min_diff = 'inf'  # Инициализируем min_diff как бесконечность

        def inorder(node, prev):
            if not node:
                return prev

            prev = inorder(node.left, prev)  # Рекурсивно обходим левое поддерево

            if prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - prev))  # Обновляем min_diff

            prev = node.val
            prev = inorder(node.right, prev)  # Рекурсивно обходим правое поддерево

            return prev

        inorder(root, None)  # Начинаем обход в порядке in-order от корня

        return self.min_diff