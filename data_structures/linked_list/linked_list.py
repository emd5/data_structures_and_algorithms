from node import Node
from typing import Any


class LinkedList(object):
    def __init__(self):
        self.head: Node = None
        self._length: int = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def insert(self, val):
        """
        This takes any value as an argument and adds that value to the head of the list.
        """
        self.head = Node(val, self.head)
        self._length += 1

    def includes(self, val):
        """
        This takes any value and returns a boolean if the value exist
        as a node value within a list
        """
        current = self.head

        while current._next is not None:
            if current.val == val:
                return True
            current = current._next

        return False

    def append(self, val):
        """
        Adds a new node with the given value to the end of the list
        """
        current = self.head
        while current.next is not None:
            current = current._next
        current._next = Node(val)

    def insert_before(self, val, new_value):
        """
        Adds a new node with the given newValue immediately before the first value node
        """
        current = self.head
        while current._next.val is not val:
            current = current._next
        new_node = Node(new_value, current._next)
        current._next = new_node

    def insert_after(self, val, new_value):
        """
        Adds a new node with the given newValue immediately after the first value node
        """
        current = self.head
        while current.val is not val:
            current = current._next
        current._next = Node(new_value, current._next)
