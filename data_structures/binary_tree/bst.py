class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

    def __repr__(self):
        print(f'')

    def __str__(self):
        print(f'')


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

    def __str__(self):
        print(f'')

    def __repr__(self):
        print(f'')

    def insert(self, value):
        """Insert a new node into the tree. """

        try:
            # if root is none insert
            if self.root is not None:
                self.root = Node(value)

            # if value is < current node
            if value < self.val:
                self.root = Node(value, self.root.left)

            # elif value is > current node
            elif value > self.val:
                self.root = Node(value, self.root.right)
        except AttributeError:
            print('Duplicate Value')






    def in_order(self, callable=lambda node: print(node)):
        """Go left until can't go any further, visit, the go right """
        callable(some_node)

        def _walk(node=None):
            """A recursive helper method that doesn't make available elsewhere"""
            #  Base case
            if node is None:
                return

            # go left
            if node.left is not None:
                _walk(node.left)

            callable(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left until can't go any further, visit, then go right """

        def _walk(node=None):
            """A recursive helper method that doesn't make available elsewhere"""
            if node is None:
                return

            #  Visit
            callable(node)

            #  Go left
            if node.left is not None:
                _walk(node.left)

            #  Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Visit, go left until can't go any further, visit, then go right """

        def _walk(node=None):
            """A recursive helper method that doesn't make available elsewhere"""
            if node is None:
                return

            #  Go left
            if node.left is not None:
                _walk(node.left)

            #  Go right
            if node.right is not None:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)


