# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#  Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''.join([char for char in s if char.isalnum()]).lower()
        s2 = s1[::-1].lower()
        if s1 == s2:
            return True
        return False


if __name__ =='__main__':
      print(isPalindrome(s = "A man, a plan, a canal: Panama"))