# Implement a queue using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty, cannot dequeue.")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("empty, cannot peek.")
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count
    
    
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.is_empty(), my_queue.size())
print(my_queue.dequeue())
print(my_queue.peek())