# Given an integer array nums, find the subarray
#  with the largest sum, and return its sum.


# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maximumsum(arr):
    if len(arr)<= 0:
        return -1
    curr_sum = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        curr_sum = max(arr[i],arr[i]+curr_sum)
        max_sum = max(curr_sum,max_sum)
    return max_sum
    
if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximumsum(arr))