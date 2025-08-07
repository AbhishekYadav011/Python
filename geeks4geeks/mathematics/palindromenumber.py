
def checkpalindromenumber(n):
    if n <= 0:
        return False
    reverse = 0 
    temp = n
    while temp >0:
        reverse = reverse * 10 + temp % 10
        temp = temp //10 

    return reverse == n

if __name__ == '__main__':
    print(checkpalindromenumber(7))