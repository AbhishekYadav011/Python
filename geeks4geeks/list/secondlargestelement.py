"""
l1,l2,l3,....,li-1,li,....ln

first from l1 to li-1 we will have largest and second largest element then li will be our x.
1. x> lar:
    slar = lar
    lar = x
2. x== lar:
    ignore
3. x < lar:
    a. slar == x:
        ignore
    b. slar == none || slar < x:
        slar = x
"""


def second_largest_element(dummylist):
    if len(dummylist) < 1:
        return None
    lar = dummylist[0]
    slar = None
    for x in dummylist[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar is None or slar < x:
                slar = x
    return slar


if __name__ == '__main__':
    testlist = [23, 45, 87, 12, 56]
    print(second_largest_element(testlist))
