"""This program is to find the last occurrence of an element in sorted array
Time complexity : O(logn)
"""


def lastoccurrence(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            if mid == len(arr)-1 or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [5, 10, 10, 10, 20, 40, 80]
    print('Last occurrence of element at position: ', lastoccurrence(arr, 10))


