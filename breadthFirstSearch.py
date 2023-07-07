'''
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
'''


def tree_by_levels(node):
    if node:
        returnList = []
        queue = [node]
        while len(queue) > 0:
            currentValue = queue.pop(0)
            returnList.append(currentValue.value)
            if currentValue.left:
                queue.append(currentValue.left)
            if currentValue.right:
                queue.append(currentValue.right)
        return returnList
    else: return []