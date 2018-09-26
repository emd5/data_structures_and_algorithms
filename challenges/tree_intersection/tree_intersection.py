class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node  | Value: {self.value} | Left: {self.left} | Right: {self.right}'

    def __str__(self):
        return f'Node  | Value: {self.value} | Left: {self.left} | Right: {self.right}'


def tree_intersection(bt1, bt2):
    common_dict = {}
    output_list = []
