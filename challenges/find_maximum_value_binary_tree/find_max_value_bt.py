def find_max_value_in_bt(binary_tree):
    visit_list = []

    if binary_tree is None:
        return IndexError('Empty list')

    max_value = binary_tree.root
    if binary_tree:
        visit_list.append(max_value)

    while visit_list:
        current = binary_tree.root
        if current.right:
            if visit_list[0].right:
                visit_list.append(visit_list[0])
        if current.left:
            if visit_list[0].left:
                visit_list.append(visit_list[0])

        if max_value > current:
            max_value = visit_list[0]
        visit_list.pop[0]
    return max_value





