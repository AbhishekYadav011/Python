
def countdigits(n):
    count = 0 
    while n> 0:
        n= n//10
        count += 1
    return count

        
if __name__ == '__main__':
    print(12//10)
    print("count of digits is:",countdigits(789))