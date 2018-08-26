from .node import Node


class Queue(object):
    def __init__(self):
        self.front: Node = None
        self._length: int =0

    def __str__(self):
        return f'Front: {self.front} | Length: {self._length}'

    def __repr__(self):
        return f'<Queue | Front: {self.front} | Length: {self._length}'

    def __len__(self):
        return self._length

    def enqueue(self, val):
        """Which takes any value as an argument and adds that value to the back of the queue """
        pass

    def dequeue(self):
        """Which takes no arguments and removes / returns the Node at the front of the queue"""
        pass



