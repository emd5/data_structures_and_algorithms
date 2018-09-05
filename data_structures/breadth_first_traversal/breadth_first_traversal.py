def breadth_first_traversal(root):
    """Method which takes a Binary Tree as its unique input. Prints every visited node’s value. """
    visited = []

    if root:
        visited.append(root)
    current = root
    while current:
        if current.left:
            visited.append(current.right)
        if current.right:
            visited.append(current.right)
        print(visited.pop(0))
        if not visited:
            break
        current = visited[0]
