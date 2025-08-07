def digitsInFactorial(N):
        fact = factorial(N)
        count = 0
        print(fact)
        while fact > 0:
            fact = fact//10
            count +=1
        return count

def factorial(N):
      if N <=1:
            return 1
      return N * factorial(N-1)

if __name__ == '__main__':
     print(digitsInFactorial(5))