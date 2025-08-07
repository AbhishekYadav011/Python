"""This program is for selection sort,
in this we search for minimum value first and swap it to starting position of array.
Time complexity : theta(n^2)
NOT stable as order of identical element is not maintained after sorting.
"""


def selectionsort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


if __name__ == '__main__':
    arr = [23, 5, 78, 10, 58]
    print(selectionsort(arr))
