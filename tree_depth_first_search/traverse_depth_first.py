

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path(root, s):
    return traverse_recursive(root, 0, s)


def traverse_recursive(currentNode, currentSum, maxSum):
    if not currentNode:
        if currentSum == maxSum:
            return True
        return False

    return traverse_recursive(currentNode.left, currentSum+currentNode.value, maxSum) \
           or traverse_recursive(currentNode.right, currentSum+currentNode.value, maxSum)





def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()