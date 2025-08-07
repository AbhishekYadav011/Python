"""Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from
that element. Find the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then you cannot move through that element."""


def minJumps(arr, n):
    # zero jump requires to reach the 1st or negative size
    if n <= 1:
        return 0
    # if start step is zero then we cannot jump to next index
    if arr[0] == 0:
        return -1
    # to hold the maximum reachable index
    maxReach = arr[0]

    # to hold the number of steps we can still take
    steps = arr[0]

    # to hold the amount of jumps to reach the maximum reachable position
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps
        # updating maxReach
        maxReach = max(maxReach, i + arr[i])
        # we use a step to get to the current index
        steps -= 1
        # If no further steps left
        if steps == 0:
            # we must have used a jump
            jumps += 1
            # Check if the current index / position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1
            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            steps = maxReach - i
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    size = len(arr)
    print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))
