def selection(unsorted):
    """A sorting algorithm using selection sort where it assigns a min then iterates
    through the list of unsorted elements and swaps if the current is less than the minimum"""
    for position in range(len(unsorted)):
        minimum = position
        for j in range(position+1, len(unsorted)):
            if unsorted[minimum] > unsorted[j]:
                minimum = j
        unsorted[position], unsorted[minimum] = unsorted[minimum], unsorted[position]
    return unsorted

