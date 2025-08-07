"""This program is to count the number of occurence of an element in the sorted array
Time complexity : O(logn)
"""
from ds.searching.firstoccurence import firstoccurence
from ds.searching.lastoccurrence import lastoccurrence


def countofoccurence(arr, x):
    first = firstoccurence(arr, x)
    if first == -1:
        return 0
    else:
        return lastoccurrence(arr, x) - first + 1


if __name__ == '__main__':
    arr = [5, 10, 10, 10, 20, 40, 80]
    print('Total count of element is:', countofoccurence(arr, 10))
