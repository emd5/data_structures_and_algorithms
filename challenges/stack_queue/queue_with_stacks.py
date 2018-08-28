from data_structures.stack.node import Node
from data_structures.stack.stack import Stack


stack1 = Stack()
stack2 = Stack()


def enqueue(self,val):
    """This method inserts value into the Queue using FIFO using stacks push pop methods. """
    node = Node(val, self.top)
    stack1.push(node)
    return self.top


def dequeue():
    """This method extracts a value from the queue using FIFO using stacks push pop methods.
    :return:
    """
    if stack2.top is not None:
        return stack2.pop()
    while stack1.top is not None:
        node = stack1.pop()
        stack2.push(node)
        return stack1.pop()







