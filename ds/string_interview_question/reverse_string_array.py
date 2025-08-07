# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


def reverseString(s):
    result = []
    for i in range(len(s)-1,-1,-1):
        result.append(s[i])
    print(result)


if __name__ == '__main__':
    s=["h","e","l","l","o"]
    reverseString(s)