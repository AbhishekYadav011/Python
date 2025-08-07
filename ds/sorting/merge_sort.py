# https://www.geeksforgeeks.org/merge-sort/

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    arr = [12, 6, 89, 45, 32, 99, 109]
    print("Array before sorting", end="\n")
    printlist(arr)
    print("Array after sorting", end="\n")
    mergesort(arr)
    printlist(arr)
