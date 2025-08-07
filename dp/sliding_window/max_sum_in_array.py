# Sliding window technique
# https://www.geeksforgeeks.org/window-sliding-technique/

def maxSum(arr, k):
    n = len(arr)
    print(n)
    if n < k:
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        #print(i)
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [1, 2, 3, 4, 5]
k = 2
print(maxSum(arr, k))
