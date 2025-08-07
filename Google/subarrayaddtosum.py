"""For a given unsorted array “X,” consisting of non-negative integers,
write a code to find the contiguous subarray that adds to the sum “S” of non-negative integers in the array."""


def addstosum(arr, sum_):
    n = len(arr)
    curr_sum = arr[0]
    start = 0
    i = 1

    while i < n:

        while curr_sum > sum_ and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum_:
            print(f"sum found b/w start index is {start} and end index is {i - 1}")
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    print("sum not found")


if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    sum_ = 23
    addstosum(arr, sum_)
