def breadth_first_traversal(root):
    """Method which takes a Binary Tree as its unique input. Prints every visited node’s value. """
    to_visit = []
    visited = []
    if root:
        to_visit.append(root)
    while to_visit:
        current = to_visit.pop(0)
        if current is not None:
            visited.append(current.value)
            # print(current.value)
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)
    return visited



