# from data_structures.queue.queue import Queue
from data_structures.queue.node import Node


class AnimalShelter(object):
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

    def enqueue(self, animal):
        """Adds animal to the shelter. animal can be either a dog or a cat object.
        :param animal: a string animal argument
        """
        temp = self.rear
        self.rear = Node(animal, self.rear)
        temp._next = self.rear

    def dequeue(self, pref):
        """A method that returns the longest waiting cat or dog.
        :param pref: a string animal argument
        :return: a string of either a dog or a cat.
        """
        if pref == 'cat':
            longest_animal = self.front
        elif pref == 'dog':
            longest_animal = self.front
        else:
            return 'dog'

        self.front = longest_animal._next
        longest_animal._next = None
        return longest_animal





