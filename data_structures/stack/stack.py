from .node import Node


class Stack(object):
    def __init__(self):
        """An instance method of the stack object. """
        self.top: Node = None
        self._length: int = 0

    def __str__(self):
        """A string representation of the stack object. """
        return f'Top: {self.top} | Length: {self._length}'

    def __repr__(self):
        """An 'official' string reputation of the stack object. """
        return f'<Stack| Top: {self.top} | Length: {self._length}'

    def __len__(self):
        """The length of the stack"""
        return self._length

    def push(self, node):
        """Which takes any value as an argument and adds that value to the top of the stack. """
        node._next = self.top
        self.top =node

    def pop(self):
        """Which takes no arguments and removes / returns the Node at the top of the stack. """
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp

    def peek(self):
        """Which takes no arguments and returns the Node at the top of the stack. """
        return self.top
