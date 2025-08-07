"""Time complexity : O(logn)"""


def binarysearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    print('Element is found at position:', binarysearch(arr, 10))

# def binarysearch(arr, l, r, x):
#     if r >= l:
#         mid = l + (r - l) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarysearch(arr, l, mid - 1, x)
#         else:
#             return binarysearch(arr, mid + 1, r, x)
#
#     else:
#         return -1
#
#
# arr = [2, 3, 4, 10, 40]
# x = 10
# result = binarysearch(arr, 0, len(arr) - 1, x)
# if result != -1:
#     print("Element is present at index %d" % result)
# else:
#     print("element is not present in array")
