
def sum_natural_number(n):
    if n <= 0:
        return 0
    return n* (n+1)/2

if __name__ == '__main__':
    print(sum_natural_number(4))