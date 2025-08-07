"""This is the optimized bubble sorting method ,when list is already sorted
Time complexity: theta(n)
Stable by nature
"""


def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        swap = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            return arr
    return arr


if __name__ == '__main__':
    arr = [78, 2, 3, 10, 20]
    print(bubblesort(arr))
