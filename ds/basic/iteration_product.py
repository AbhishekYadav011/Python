from itertools import product


def cartesian_product(arr1, arr2, arr3):
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2, arr3))


# Driver Function
if __name__ == "__main__":
    arr1 = [5, 4]
    arr2 = [7, 8, 9]
    arr3 = [5, 7, 8, 9, 10]
    print(cartesian_product(arr1, arr2, arr3))
