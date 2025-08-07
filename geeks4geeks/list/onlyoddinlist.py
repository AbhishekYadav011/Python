"""
Find out only odd occurrence of a number in list
    List: [10,20,30,10,20]
    output: 30
"""


def odd_occurrence(dummylist):
    results = 0
    for i in dummylist:
        count = dummylist.count(i)
        if count % 2 != 0:
            results = i
            break
    return results


"""
Bitwise operator to find out only odd in the given list
"""


def odd_occurence_using_xor(dummylist):
    results = 0
    for x in dummylist:
        results = results ^ x
    return results


if __name__ == '__main__':
    l1 = [10, 20, 30, 10, 20]
    print("odd occurrence is:", odd_occurrence(l1))
    print("odd occurrence using bitwise operator XOR is:", odd_occurence_using_xor(l1))
