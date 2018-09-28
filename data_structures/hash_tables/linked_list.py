class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Next: {self.next}>'


class LinkedList(object):
    def __init__(self, iterable=[]):
        """Instantiates the LL object. """
        self.head: Node = None
        self._length: int = 0
        for i in iterable:
            self.insert(i)

    def __str__(self):
        """A string representation of the LL object. """
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        """ An official string representation of the LL object. """
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        """The length of the LL. """
        return self._length

    def insert(self, val):
        """This takes any value as an argument and adds that value to the head of the list. """
        try:
            if self.head is None:
                self.head = Node(val, self.head)
                self._length += 1
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        except AttributeError:
            return f'The head is {self.head}'

    def includes(self, val):
        """Accepts an value argument, returns a boolean if the value exist as a node value within a list. """
        current = self.head

        while current.next is not None:
            if current.val == val:
                return True
            current = current.next

        return False

    def append(self, val):
        """Adds a new node with the given value to the end of the list. """
        if self.head is None:
            self.head = Node(val)
            self._length += 1

        current = self.head

        while current.next is not None:
            current = current.next
        new_node = Node(val)
        self._length += 1
        current.next = new_node

    def insert_before(self, val, new_value):
        """Adds a new node with the given newValue immediately before the first value node. """

        current = self.head

        if current.val is val:
            self.insert(new_value)
        else:
            while current.next.val is not val:
                current = current.next

            new_node = Node(new_value, current.next)
            # new_node._next = current._next
            current.next = new_node
            self._length += 1

    def insert_after(self, val, new_value):
        """Adds a new node with the new value immediately after the first value node. """
        current = self.head

        while current.val is not val:
            current = current.next
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        self._length += 1

        if current.next is None:
            current.next = Node(new_value)
            self._length += 1


