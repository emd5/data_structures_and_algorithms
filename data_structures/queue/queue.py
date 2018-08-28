from .node import Node


class Queue(object):
    def __init__(self):
        """An instance method of the queue object. """
        self.front: Node = None
        self.rear: Node = None
        self._length: int = 0

    def __str__(self):
        """A string representation of the queue object. """
        return f'Front: {self.front} | Length: {self._length}'

    def __repr__(self):
        """An 'official' string reputation of the queue object. """
        return f'<Queue | Front: {self.front} | Length: {self._length}'

    def __len__(self):
        """The length of the queue. """
        return self._length

    def enqueue(self, val):
        """Which takes any value as an argument and adds that value to the back of the queue. """
        temp = self.rear
        self.rear = Node(val, self.rear)
        temp._next = self.rear

    def dequeue(self):
        """Which takes no arguments and removes / returns the Node at the front of the queue. """
        temp = self.front
        self.front = temp._next
        temp._next = None
        return temp

    def peek(self):
        return self.front



