def breadth_first_traversal(root):
    """Method which takes a Binary Tree as its unique input. Prints every visited node’s value. """
    visited = []

    if root:
        visited.append(root)
    current = root
    while current:
        if current.left:
            print(current.left.value)
            visited.append(current.left)
        if current.right:
            print
            print(current.right.value)
            visited.append(current.right)

        print(visited.pop(0))

        if not visited:
            break
        current = visited[0]
