# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twosum(nums,target):
    res = set()
    for num in nums:
            complement = target - num
            """"And condition is required in below IF condition for a use case of  [3,3] and target = 6"""
            if complement in res and complement != num:
                return [nums.index(complement),nums.index(num)]
            elif complement in res:
                return [nums.index(complement),nums.index(num,nums.index(num)+1)]
            res.add(num)
    return False    






if __name__ == '__main__':
    arr = [2,7,11,15]
    target = 9
    print(twosum(arr,target))