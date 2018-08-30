class Node(object):
    def __init__(self, val, _next=None):
        """A constructor method for the Node class
        :param val: The value of the Node
        :param _next: A pointer reference to the next node
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """The string representation of the Node object
        :return: A string value of the Node
        """
        return f'{self.val}'

    def __repr__(self):
        """The "official" string reputation of a Node object
        :return: A node string value and next node
        """
        return f'<Node | Val: {self.val} | Next: {self._next}'
