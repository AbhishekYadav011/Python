"""Given a number n, write an efficient function to print all prime factors of n. 
For example, 
if the input number is 12, then the output should be “2 2 3”."""

import math

def checkprimenumber(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primefactor(n):
    for i in range(2, n+1):
        if checkprimenumber(i):
            x = i
            while n % x == 0:
                print(i)
                x = x* i
            
if __name__ == '__main__':
    primefactor(100)


