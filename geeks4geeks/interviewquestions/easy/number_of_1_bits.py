# Given a positive integer n, write a function that returns the number of 
# set bits
#  in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n&(n-1)
            count +=1
        return count
if __name__ == '__main__':
      print(hammingWeight(n = 11))
