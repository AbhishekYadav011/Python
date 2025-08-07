def largest_element(dummylist):
    if not dummylist:
        return None
    else:
        results = dummylist[0]
        for i in range(1, len(dummylist)):
            if dummylist[i] > results:
                results = dummylist[i]
        return results


if __name__ == '__main__':
    testlist = [23, 56, 21, 80]
    print(largest_element(testlist))
