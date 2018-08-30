from data_structures.stack.stack import Stack
# from .node import Node


def multi_bracket_validation(input):
    stack = Stack()

    counter = 0
    for letter in input:
        counter += 1
        print(str(counter) + ' ' + letter)
        if letter == '(' or letter == '{' or letter == '[':
            print(letter)
            stack.push(letter)


        if letter == ')' or letter == '}' or letter == ']':
            print(letter)
            stack.pop()
            return
            # if stack.peek() == ')':
            #     print(letter)
            #     print(stack.pop())
        # if letter == '{':
        #     print(letter)
        #     stack.push(letter)
            # if stack.peek() == ')':
            #     print(letter)
            #     print(stack.pop())
        # if letter == '[':
        #     print(letter)
        #     stack.push(letter)
            # if stack.peek() == ')':
            #     print(letter)
            #     print(stack.pop())

    # while stack.top is not None:
    #     if stack.peek() == ')':
    #         print(letter)
    #         print(stack.pop())
    #     if stack.peek() == ')':
    #         print(letter)
    #         print(stack.pop())
    #     if stack.peek() == ')':
    #         print(letter)
    #         print(stack.pop())




multi_bracket_validation("({[]})")
