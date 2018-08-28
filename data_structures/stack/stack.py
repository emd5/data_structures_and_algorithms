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
        return f'<Stack | Top: {self.top} | Length: {self._length}'

    def __len__(self):
        """The length of the stack. """
        return self._length

    def push(self, val):
        """Which takes any value as an argument and adds that value to the top of the stack. """
        self.top = Node(val, self.top)

    def pop(self):
        """Which takes no arguments and removes / returns the Node at the top of the stack. """
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp

    def peek(self):
        """Which takes no arguments and returns the Node at the top of the stack. """
        try:
            if self.top is not None:
                return self.top
        except ReferenceError:
            print('List is empty')
