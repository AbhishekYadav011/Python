"""https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/"""


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def getverticalorder(root, hd, m):
    if root is None:
        return
    try:
        m[hd].append(root.key)
    except:
        m[hd] = root.key
    getverticalorder(root.left, hd - 1, m)
    getverticalorder(root.right, hd + 1, m)


def printverticalorder(root):
    m = dict()
    hd = 0
    getverticalorder(root, hd, m)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end=" ")
        print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print("Vertical order traversal is")
printverticalorder(root)
