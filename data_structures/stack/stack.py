from .node import Node


class Stack(object):
    def __init__(self, iterable=[]):
        """An instance method of the stack object. """
        self.top: Node = None
        self._length: int = 0
        for i in iterable:
            self.push(i)

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
        """Accepts value as an argument and adds that value to the top of the stack. """
        try:
            temp = self.top
            self.top = Node(val, self.top)
            self.top._next = temp
        except AssertionError:
            self.top = Node(val, self.top)
        self._length += 1

    def pop(self):
        """Removes the top Node in the stack. """
        try:
            temp = self.top
            self.top = temp._next
            temp._next = None
            self._length -= 1
        except AttributeError:
            return 'Stack is empty'

    def peek(self):
        """Which takes no arguments and returns the Node at the top of the stack. """
        try:
            if self.top.val is not None:
                return self.top
        except AttributeError:
            print('Stack is empty')
