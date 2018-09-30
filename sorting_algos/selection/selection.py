def selection(unsorted):
    """A sorting algorithm using selection sort where it assigns a min then iterates
    through the list of unsorted elements and swaps if the current is less than the minimum"""
    for i in range(len(unsorted)):
        minimum = i
        for j in range(i+1, len(unsorted)):
            if unsorted[minimum] > unsorted[j]:
                minimum = j
        unsorted[i], unsorted[minimum] = unsorted[minimum], unsorted[i]
    return unsorted

