"""
This program is to left rotate or anti clockwise the given list by 1.
    input: l0,l1,l2,.....,ln-1
    output: l1,l2,......,ln-1,l0

"""


def using_slicing(dummylist):
    dummylist = dummylist[1:] + dummylist[0:1]
    return dummylist


def using_inbuilt_list_method(dummylist):
    dummylist.append(dummylist.pop(0))
    return dummylist


def rotate_list_by_one(dummylist):
    n = len(dummylist)
    x = dummylist[0]
    for i in range(1, n):
        dummylist[i - 1] = dummylist[i]
    dummylist[n - 1] = x
    return dummylist


def rotateString(s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        for _ in range(len(s)):
            s = s[1:] + s[0]
            print(s)
            if s == goal:
                return True
        return False

if __name__ == '__main__':
    testlist = [10, 20, 30, 40, 50]
    # print("New list after left rotation by one:", using_slicing(testlist))
    # print("New list after left rotation by one:", using_inbuilt_list_method(testlist))
    # print("New list after left rotation by one:", rotate_list_by_one(testlist))
    print(rotateString("abcde", "cdeab"))
