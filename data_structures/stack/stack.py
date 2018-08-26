from .node import Node


class Stack(object):
    def __init__(self):
        self.top: Node = None
        self._length: int = 0

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def push(self, val):
        """Which takes any value as an argument and adds that value to the top of the stack"""
        pass

    def pop(self):
        """Which takes no arguments and removes / returns the Node at the top of the stack"""
        pass

    def peek(self):
        """Which takes no arguments and returns the Node at the top of the stack"""
        pass
