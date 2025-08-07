def partiotion(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[h], arr[i + 1] = arr[i + 1], arr[h]
    return i + 1


def quick_sort(arr, l, h):
    if l < h:
        p = partiotion(arr, l, h)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, h)


array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(f'sorted array:{array}')
