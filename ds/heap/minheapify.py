"""Implementation of Heapify  operation in Min-Heap"""
"""Below are two properties of minheap:
    1. It must be a complete binary tree.
    2. Root(parent) is always smaller than the leaf or child . """

def heapify(arr,i,n):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[smallest] > arr[left]:
        smallest = left
    if right < n and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i :
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,smallest,n)

if __name__ == "__main__":
    arr = [10, 5, 15, 2, 20, 30]
    print("Original array:", arr)
    # Perform heapify operation on a min-heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))
    print("Min-Heap after heapify operation:", arr)