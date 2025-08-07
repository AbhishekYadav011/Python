""" In insertion sort we start selecting second element and put in the correct place
Time complexity : O(n^2)
Stable and In place sorting
"""


def insertionsort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [11, 45, 10, 9, 87, 62]
print("array after sorting")
insertionsort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
