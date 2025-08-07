"""
This program is to left rotate or anti clockwise the given list by d.
    if d = 2
    input: l0,l1,l2,l3,.....,ln-1
    output: l2,l3,......,ln-1,l0,l1

"""


# Method 1
def left_rotate_by_d(dummylist, d):
    for i in range(0, d):
        dummylist.append(dummylist.pop(0))
    return dummylist


# Method 2
"""
In this method we will reverse the list 3 times 
a. First reversal will be for list upto 'd'
b. second reversal will be for remaining list element
c. Third reversal will be for entire list
"""


def left_rotate(l, d):
    n = len(l)
    reverse_a_list(l, 0, d - 1)
    reverse_a_list(l, d, n - 1)
    reverse_a_list(l, 0, n - 1)
    print(l)


def reverse_a_list(l, b, e):
    while b < e:
        l[b], l[e] = l[e], l[b]
        b += 1
        e -= 1


if __name__ == '__main__':
    testlist = [10, 20, 30, 40, 50]
    print("New list after 2 left rotation:", left_rotate_by_d(testlist, 2))
    #left_rotate(testlist, 2)
