""" euclidean approach: https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/"""

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

if __name__ == '__main__':
    a,b= 12,15
    if gcd(a,b):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print("Not found")

