"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""


def searchRange(nums, target: int):
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] == target and nums[i + 1] == target:
            return [i, i + 1]
        elif nums[i] == target and nums[i + 1] != target:
            return [i, i]

    return [-1, -1]


if __name__ == '__main__':
    testlist = [5, 7, 7, 8, 8, 10]
    print(searchRange(testlist,8))
