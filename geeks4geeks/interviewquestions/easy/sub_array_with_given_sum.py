"""Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds
to a given number S.
In case of multiple subarrays, return the subarray which comes first on moving from left to right."""


def subArraySum(arr, n, s):
    if n == 1:
        if arr[0] == s:
            return [1, 1]
        elif arr[0] != s:
            return [-1]
    i = 0
    Sum = arr[0]
    for j in range(1, n):
        Sum = Sum + arr[j]
        while Sum > s and i < j:
            Sum = Sum - arr[i]
            i += 1
            print(i, arr[i])
        if Sum == s:
            return [i + 1, j + 1]
    return [-1]


if __name__ == '__main__':
    arr = [1, 2, 3, 7, 5]
    "2+3+7=12"
    print(subArraySum(arr, 5, 12))
