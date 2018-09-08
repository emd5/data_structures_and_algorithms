from .stack import Stack


def multi_bracket_validation(string_input):
    """
    A method that accepts a string argument, checks balanced brackets to be true
    otherwise false.
    """
    stack = Stack()

    counter = 0
    for letter in string_input:
        if letter == '(' or letter == '{' or letter == '[':
            stack.push(letter)
            counter += 1
        elif letter == ')' or letter == '}' or letter == ']':
            if letter == ')' and stack.peek() == '(':
                stack.pop()
                counter -= 1
            elif letter == '}' and stack.peek() == '{':
                stack.pop()
                counter -= 1
            elif letter == ']' and stack.peek() == '[':
                stack.pop()
                counter -= 1

    if counter == 0 and stack.top is None:
        return True
    else:
        return False


