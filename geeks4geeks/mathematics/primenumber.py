import math

def checkprimenumber(n):
    print(int(math.sqrt(n)))
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        print("Inside for loop")
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(checkprimenumber(2))