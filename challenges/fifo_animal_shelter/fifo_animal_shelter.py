from data_structures.queue.queue import Queue
from data_structures.queue.node import Node


class AnimalShelter(object):

    def enqueue(self, animal):
        """Adds animal to the shelter. animal can be either a dog or a cat object.
        :param animal: a string animal argument
        """
        longest = 0
        while cat_queue is not None or dog_queue is not None:
            if not animal:
                return 'Invalid animal'
            if animal.lower() is 'cat':
                cat_node = Node(animal)



            elif animal.lower is 'dog':
                dog_node = Node(animal)



    def dequeue(self, pref):
        """A method that returns the longest waiting cat or dog.
        :param pref: a string animal argument
        :return: a string of either a dog or a cat.
        """
        if pref.lower() == 'cat':
            return cat_queue.dequeue()
        elif pref.lower() == 'dog':
            return dog_queue.dequeue()
        else:
            return 'dog'  # We prefer dog


