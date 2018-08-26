class Node(object):
    def __init__(self, val, _next=None):
        """
        A constructor method of the Node Class
        :param val: The value of the node
        :param _next: A reference pointer to the next Node
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """
        The string representation of the Node object
        :return: A value of the Node
        """
        return f'{self.val}'

    def __repr__(self):
        """
        An 'official' string reputation of a Node object
        :return: A node string value and next node
        """
        return f'<Node | val: {self.val} | next:{self._next}'
