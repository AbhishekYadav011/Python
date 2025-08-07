"""based on the formula
    HCF(a,b) * LCM(a,b) = a*b
    therefore 
    LCM(a,b) = (a*b)/HCF(a*b)

"""

def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)

def lcm(a,b):
    lcm = (a*b)//hcf(a,b)
    return lcm

if __name__ == '__main__':
    a,b = 4,6
    print("LCM of a & b is:",lcm(a,b))