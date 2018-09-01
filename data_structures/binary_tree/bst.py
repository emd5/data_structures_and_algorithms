class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

    def __repr__(self):
        print(f'Binary Tree  | Data: {self.data} | Left: {self.left} | Right: {self.right}')

    def __str__(self):
        print(f'Data: {self.left.data} | Right: {self.right}')


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None
        self.val = None
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        print(f'Binary Tree | Data: {self.data} | Left: {self.left} | Right: {self.right}')

    def __repr__(self):
        print(f'Binary Tree | Data {self.data}')

    def insert(self, value):
        """Insert a new node into the tree. """
        try:
            # if root is none insert
            if self.root is None:
                self.root = Node(value)

            current = self.root

            # Go left when value < current
            if value < current.val:
                current.left = current
                if current.left is None:
                    current.left = Node(value.data)
                else:
                    self.insert(current)

            # Go right when value < current
            elif value > current.val:
                if current.right is None:
                    current.right = Node(value.data)
                else:
                    self.insert(current)
        except AttributeError:
            print('Duplicate Value')

    def in_order(self, callable=lambda node: print(node)):
        """Go left until can't go any further, visit, the go right """
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


