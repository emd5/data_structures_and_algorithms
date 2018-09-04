class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        print(f'Node  | Value: {self.val} | Left: {self.left} | Right: {self.right}')

    def __str__(self):
        print(f'Node  | Value: {self.val} | Left: {self.left} | Right: {self.right}')


class BinaryTree(object):
    def __init__(self, iterable=[]):
        self.root = None
        for i in iterable:
            self.insert(i)

    def __str__(self):
        print(f'Binary Tree | Root: {self.root} | In order: {self.in_order()}')

    def __repr__(self):
        print(f'Binary Tree | In order {self.in_order()} | Pre Order: {self.pre_order()} '
              f'| Post Order: {self.post_order()}')

    def insert(self, value):
        """Insert a new node into the tree. """

        if self.root is None:
            self.root = Node(value)

        def _insert(current_node):
            if current_node.value < value:
                current_node.left = current_node
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    _insert(current_node)

            elif  current_node.value > value:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    _insert(current_node)

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


