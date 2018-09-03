def get_merge_list(ll_1, ll_2):

    length_1 = get_length(ll_1)
    length_2 = get_length(ll_2)

    if length_1 < length_2:
        return (merge_list(ll_1, ll_2))
    else:
        return (merge_list(ll_2, ll_1))


def merge_list(small_list, big_list):
    """The first argument is the smaller list than the second argument"""
    smaller_list = get_length(small_list)
    small = small_list.head
    big = big_list.head
    while smaller_list is not 1:
        smaller_list -= 1
        big_list.insert_before(big.val, small.val)
        small = small._next
        big = big._next
    return big_list


def get_length(ll):
    current = ll.head
    count = 0
    while current is not None:
        current = current._next
        count += 1
    return count




