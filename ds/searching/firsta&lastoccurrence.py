"""Find the first and last occurrence of a number in a list, if number is not present return [-1,-1]"""


def first_last_occurrence(templist, number):
    first = last = -1
    for i in range(len(templist)):
        if templist[i] != number:
            continue
        if first == -1:
            first = i
        last = i
    return [first, last]


if __name__ == '__main__':
    templist = [10, 8, 23, 90, 8, 78]
    print(first_last_occurrence(templist, 8))
