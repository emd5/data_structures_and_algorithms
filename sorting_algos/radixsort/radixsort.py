def radix_sort(unsorted):
    """A Radix sort that takes an unsorted list and evaluates at
    each place of a value, sorts based on the value and returns
    a sorted list"""
    unsorted_length = len(unsorted)
    modulus = 10
    div = 1

    while True:
        new_list = [[] for x in range(10)]
        for value in unsorted:
            least_digit = value % modulus
            least_digit /= div
            new_list[int(least_digit)].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == unsorted_length:
            return new_list[0]

        unsorted = []
        for x in new_list:
            for y in x:
                unsorted.append(y)

