from random import randint


def quicksort(arr):
    """A quicksort method that randomly selects a pivot and compares the index against the pivot"""
    if len(arr) <= 1:
        return arr
    left_array = []
    mid = []
    right_array = []
    pivot = arr[randint(0, len(arr)-1)]

    for i in arr:
        if i < pivot:
            left_array.append(i)
        elif i == pivot:
            mid.append(i)
        else:
            right_array.append(i)
    return quicksort(left_array) + mid + quicksort(right_array)

