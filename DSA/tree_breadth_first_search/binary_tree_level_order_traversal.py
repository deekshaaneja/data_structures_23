
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right=right

def traverse(root):
    q = deque()
    q.append(root)
    ls = []
    while q:
        levelSize = len(q)
        levells = []
        for _ in range(levelSize):
            current_node = q.popleft()
            levells.append(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        ls.append(levells)
    return ls

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()






