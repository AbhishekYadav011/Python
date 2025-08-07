# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:https://leetcode.com/problems/happy-number/


def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            total = 0 
            while n > 0:
                digit = n % 10
                total = total + digit ** 2
                n //= 10
            n = total

            if n in seen:
                return False
            seen.add(n)
        return True

if __name__ == '__main__':
     print(isHappy(19))