"""The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.
https://www.geeksforgeeks.org/sieve-of-eratosthenes/"""

# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfErathenes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.

    prime = [True for i in range(n+1)]

    p=2 
    while (p*p<= n):
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p +=1

    for i in range(2,n+1):
        if prime[i] == True:
            print(i)

if __name__ == '__main__':
    SieveOfErathenes(10)