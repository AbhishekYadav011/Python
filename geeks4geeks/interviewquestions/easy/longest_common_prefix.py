# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        print(strs)
        low = strs[0]
        high = strs[-1]
        minLength = min(len(low),len(high))
        print(minLength)
        i = 0
        while i< minLength and low[i] == high[i]:
            i += 1
        return low[:i]

if __name__ == '__main__':
      print(longestCommonPrefix(strs = ["flower","flow","flight"]))