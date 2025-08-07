"""You’re given an array “arr” of size “n,”
containing sets of 0s, 1s, and 2s. Write a program to sort the array elements in ascending order."""


def sortarray(arr, n):
    count0 = 0
    count1 = 0
    count2 = 0

    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        if arr[i] == 1:
            count1 += 1
        if arr[i] == 2:
            count2 += 1
    i = 0
    while count0 > 0:
        arr[i] = 0
        i += 1
        count0 -= 1
    while count1 > 0:
        arr[i] = 1
        i += 1
        count1 -= 1
    while count2 > 0:
        arr[i] = 2
        i += 1
        count2 -= 1
    return arr


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(sortarray(arr, len(arr)))
