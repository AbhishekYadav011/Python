# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

def rotateanarray(arr, d, n):
    arr[:] = arr[d:n] + arr[0:d]
    return arr


if __name__ == "__main__":
    arr = [4, 2, 9, 0, 3, 6, 7, ]
    print(arr)
    print("after rotation")
    print(rotateanarray(arr, 3, len(arr)))
