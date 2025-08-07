"""Time complexity : O(n^2)
Stable by nature
"""


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [11, 13, 89, 62, 78]
print("array before sorting")
printlist(arr)
bubblesort(arr)
print("array after sorting")
printlist(arr)
