class Node(object):
    def __init__(self, val, _next=None):
        """
        A constructor method of the Node Class
        :param val: The value of the node
        :param _next: A reference pointer to the next Node
        """
        self.val = val
        self._next = _next
        self.front = None
        self.rear = None

    def __str__(self):
        """
        The string representation of the Node object
        :return: A value of the Node
        """
        return f'Queue Node  | Value: {self.val}| Next: {self._next}'

    def __repr__(self):
        """
        An 'official' string reputation of a Node object
        :return: A node string value and next node
        """
        return f'<Queue Node | Value: {self.val} | Next:{self._next}'
