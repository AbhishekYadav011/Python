"""Find first non-repeating character of given string
Input: s = “geeksforgeeks”
Output: ‘f’
Explanation: ‘f’ is the first character in the string which does not repeat.
"""

# def nonrepeatingchar(s):
#     if len(s) == 1:
#         return s[i]
#     for i in range(len(s)):
#         if s[i] not in s[i+1:len(s)]:
#             return s[i]
#     return None


def nonrepeatingchar(s):
  
    # Initialize frequency array
    freq = [0] * 26

    # Count the frequency of all characters
    for c in s:
        freq[ord(c) - ord('a')] += 1

    # Find the first character with frequency 1
    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == 1:
            return s[i]
    
    # If no character with a frequency of 1 is 
    # found, then return '$'
    return '$'


if __name__ == "__main__":
    teststring = "geeksforgeeks"
    result = nonrepeatingchar(teststring)
    print("left most non repeating character:",result)