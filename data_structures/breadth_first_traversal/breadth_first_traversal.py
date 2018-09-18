from .queue import Queue


def breadth_first_traversal(tree):
    """Accepts a Binary Tree as its unique input. Prints every compare_list node’s value."""
    q = Queue()
    bfs_list = []

    if tree is None:
        return AssertionError('No tree found')

    def _walk(tree):
        """A recursive helper method that traverses through the tree"""

        if q.front is None:
            return 'Empty Queue'

        if tree.root is None:
            return 'No binary tree'

        if tree.root:
            q.enqueue(tree)
            # bfs_list.append(q.peek())

        if tree.root.right is not None:
            q.enqueue(tree.root.right)
            # bfs_list.append(q.peek())

        if tree.root.left is not None:
            q.enqueue(tree.root.left)
            # bfs_list.append(q.peek())

        bfs_list.append(q.peek())
        q.dequeue()

    _walk(tree)

    return bfs_list



