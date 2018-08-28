from ../queue import queue
from ../stack import stack


def queues_with_stacks():
    """
    This method implements a queue with two stacks
    :return:
    """
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    queue.dequeue()
    queue.enqueue()


