def is_list_sorted(dummylist):
    if not dummylist or len(dummylist) < 1:
        return True
    else:
        for i in range(1, len(dummylist)):
            if dummylist[i] < dummylist[i - 1]:
                return False
        return True


if __name__ == '__main__':
    l1 = [10, 20, 40]
    if is_list_sorted(l1):
        print("Yes")
    else:
        print("No")
