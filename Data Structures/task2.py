#Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def is_balanced(sequence):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in sequence:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty():
                return False
            if brackets[stack.pop()] != char:
                return False

    return stack.is_empty()


print(is_balanced('()))(')) #false
print(is_balanced("[[[{}]]]")) #true