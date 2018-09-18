class Node:
    def __init__(self, val, data=None, left=None, right=None):
        """Attributes for the Binary Tree Class"""
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """An official string representation of a Node in the Binary Tree. """
        return f'{self.value}'

    def __str__(self):
        """A string representation of a node in the Binary tree. """
        return f'{self.value}'


class BinaryTree(object):
    def __init__(self, iterable=[]):
        """Constructor for the Binary Tree class"""
        self.root = None

        if iterable is None:
            iterable = []

        for i in iterable:
            self.insert(i)

    def __str__(self):
        """A string representation of the Binary Tree """
        return f'BT | {self.root} {self.root.left} {self.root.right} =>'

    def __repr__(self):
        """An official string represenation of the Binary Tree """
        return f'BT | {self.root} {self.root.left}  {self.root.right} =>'

    def insert(self, value):
        """Insert a new node into the tree. Returns a node """
        node = Node(value)

        if self.root is None:
            self.root = node
            return node

        current = self.root
        while current:
            if value == current.value:
                raise ValueError('Value already exist')

            if value < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left

            if value > current.value:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

        return node

    def in_order(self, callable=lambda node: print(node)):
        """Go left until can't go any further, visit, the go right. """

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
        """Visit, go left until can't go any further, visit, then go right. """
        def _walk(node=None):
            """A recursive helper method that doesn't make available elsewhere. """
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
        """ go left until can't go any further then go right, then visit. """
        def _walk(node=None):
            """A recursive helper method that doesn't make available elsewhere. """
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
