from .linked_list import LinkedList


def merge_list(ll_1, ll_2):

    ll_3 = LinkedList()
    current_1 = ll_1.head
    current_2 = ll_2.head

    while current_1 is not None or current_2 is not None:
        if current_1 is not None:
            ll_3.append(current_1.val)
            current_1 = current_1._next
        if current_2 is not None:
            ll_3.append(current_2.val)
            current_2 = current_2._next
    return ll_3


