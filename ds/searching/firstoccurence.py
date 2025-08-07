"""This program is to find the first occurrence of an element in sorted array
Time complexity : O(logn)
"""


def firstoccurence(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if x < arr[mid]:
            high = mid - 1

        elif x > arr[mid]:
            low = mid + 1

        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    arr = [5, 10, 10, 10, 20, 40, 80]
    print('First occurrence of element at position: ', firstoccurence(arr, 10))
