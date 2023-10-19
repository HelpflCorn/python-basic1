#Implement a stack using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty, no pop for you")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty, no peek for you")
        return self.top.data

    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count

