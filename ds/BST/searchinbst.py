"""Search operations in binary search tree
Time complexity: O(logn)"""


def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)
