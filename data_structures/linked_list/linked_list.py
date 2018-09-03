from .node import Node


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
            self.head._next = temp
        except AttributeError:
            return f'The head is {self.head}'

    def includes(self, val):
        """Accepts an value argument, returns a boolean if the value exist as a node value within a list. """
        current = self.head

        while current._next is not None:
            if current.val == val:
                return True
            current = current._next

        return False

    def append(self, val):
        """Adds a new node with the given value to the end of the list. """
        if self.head is None:
            self.head = Node(val)
            self._length += 1

        current = self.head

        while current._next is not None:
            current = current._next
        new_node = Node(val)
        self._length += 1
        current._next = new_node

    def insert_before(self, val, new_value):
        """Adds a new node with the given newValue immediately before the first value node. """

        current = self.head

        if current.val is val:
            self.insert(new_value)
        else:
            while current._next.val is not val:
                current = current._next

            new_node = Node(new_value, current._next)
            # new_node._next = current._next
            current._next = new_node
            self._length += 1

    def insert_after(self, val, new_value):
        """Adds a new node with the new value immediately after the first value node. """
        current = self.head

        while current.val is not val:
            current = current._next
        new_node = Node(new_value)
        new_node._next = current._next
        current._next = new_node
        self._length += 1

        if current._next is None:
            current._next = Node(new_value)
            self._length += 1

    def kth_from_the_end(self, val):
        """
        Takes in a value length_of_list
        :param
            val: The target node value
        :return:
            Returns a node of the value from the end of the LL
        """
        try:
            length_of_list = 0
            current = self.head

            while current._next is not None:
                length_of_list += 1
                current = current._next

            # if val > length_of_list:
            #     return 'Exception'

            count = length_of_list - val
            current = self.head
            while count is not 1:
                count -= 1
                current = current._next

            return current.val
        except AttributeError:
            return 'Your value is greater than length of list'




