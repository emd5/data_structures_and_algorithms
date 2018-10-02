def mergesort(arr):
    """A method using MergeSort that accepts an unsorted array and returns a sorted array"""

    arr_length = len(arr)
    if arr_length > 1:
        mid = arr_length // 2
        left_half = mergesort(arr[:mid])
        right_half = mergesort(arr[mid:])
        i = 0
        j = 0
        k = 0
        l_length = len(left_half)
        r_length = len(right_half)
        while i < l_length and j < r_length:
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < l_length:
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < r_length:
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr



