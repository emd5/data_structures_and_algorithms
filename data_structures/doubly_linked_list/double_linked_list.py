class Node:
    def __init__(self, val, _next=None, _previous=None):
        self.value = val
        self._next = _next
        self._previous = _previous

    def __repr__(self):
        return f'<Node | Val: {self.value} | Next: {self._next} | Previous: {self._previous}>'

    def __str__(self):
        return f'{self.value}'


class DoublyLinkedList(object):
    def __init__(self, iterable=[]):
        self.head: Node = None
        self._length: int = 0
        for i in iterable:
            self.insert(i)

    def __str__(self):
        """A string representation of the DLL object. """
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        """ An official string representation of a DLL object. """
        return f'<DLL | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        """The length of a DLL"""
        return self._length

    def insert(self, data):
        """adds that value to the head of the list"""
        try:
            if self.head is None:
                self.head = Node(data, self.head)
                self._length += 1
            else:
                temp = self.head
                self.head = Node(data)
                self.head._next = temp
                self.head._previous = None
                self._length += 1
        except AttributeError:
            return f'The head is {self.head}'

    def append_in_middle(self, previous_node, data):
        """Adding new node in middle of dll"""

        if self.head is None:
            self.head = Node(data, self.head)
            self._length += 1

        current = self.head

        # while current._next is not None:
        #     if current == previous_node:
        #         temp = current._next
        #
        #
        #
        # current = current._next





    def remove(self, val):
        pass

    def find(self, val):
        pass
