def divisors(n):
    i = 1
    while(i*i < n):
        if n % i == 0:
            print(i)
        i +=1
    while (i >=1):
        if n%i == 0:
            print(n//i)
        i -=1

if __name__ == '__main__':
    divisors(15)