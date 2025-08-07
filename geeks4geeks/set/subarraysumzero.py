"""Given an array of positive and negative numbers,
 find if there is a subarray (of size at-least one) with 0 sum."""


def subArrayExists(arr):
    s = set()
    n_sum = 0
    for i in range(len(arr)):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False


if __name__ == '__main__':
    arr = [-3, 2, 3, 1, 6]
    print(subArrayExists(arr))
    arr1 = [1, 4, -2, -2, 5, -4, 3]
    print(subArrayExists(arr1))
