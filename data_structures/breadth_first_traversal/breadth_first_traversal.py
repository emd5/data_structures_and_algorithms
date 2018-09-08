def breadth_first_traversal(tree):
    """Accepts a Binary Tree as its unique input. Prints every compare_list node’s value."""
    to_visit = []
    compare_list = []
    if tree:
        to_visit.append(tree)

    while current:
        current = to_visit.pop(0)
        if current is not None:
            compare_list.append(current)
        if current.left:
            to_visit.append(current)
        if current.right:
            to_visit.append(current)
    return compare_list
    # to_visit = []
    # compare_list = []
    # if tree:
    #     to_visit.append(tree)
    # while to_visit:
    #     current = to_visit.pop(0)
    #     if current is not None:
    #         compare_list.append(current.value)
    #     if current.left:
    #         to_visit.append(current.left)
    #     if current.right:
    #         to_visit.append(current.right)
    # return compare_list



