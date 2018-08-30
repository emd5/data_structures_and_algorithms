from .stack import Stack


def multi_bracket_validation(string_input):
    """
    A method that accepts a string argument, checks balanced brackets to be true
    otherwise false.
    """
    stack = Stack()

    counter = 0

    for letter in string_input:
        counter += 1
        if letter == '(' or letter == '{' or letter == '[' and stack is None:
            stack.push(letter)
        if letter == ')' or letter == '}' or letter == ']' and stack is None:
            stack.pop()

    if stack.top is None:
        return True
    else:
        return False
