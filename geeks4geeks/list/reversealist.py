"""
This program is to reverse a list by own function
 input:l0,l1,l2,.....,ln-3,ln-2,ln-1
 output:ln-1,ln-2,ln-3,.........,l2,l1,l0
 :here we need to swap values between start and endpoint and stop in below two condition
    a:when start equals to endpoint in case of odd list
    b:when start is greater than endpoint
"""


def reverse_list(dummylist):
    start = 0
    end = len(dummylist) - 1
    while start < end:
        dummylist[start], dummylist[end] = dummylist[end], dummylist[start]
        start += 1
        end -= 1
    return dummylist


if __name__ == '__main__':
    l1 = [10, 20, 30, 40, 50]
    print("reversd list is:", reverse_list(l1))
