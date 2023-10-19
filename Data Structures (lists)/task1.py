#Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two parameters 'start' and
# 'stop', and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found")

    def pop(self, position=None):
        if position is None:
            if self.head is None:
                raise IndexError("pop from empty list")
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            if position < 0:
                raise IndexError("out of range")
            if position == 0:
                return self.pop()
            current = self.head
            previous = None
            index = 0
            while current is not None and index < position:
                previous = current
                current = current.next
                index += 1
            if current is None:
                raise IndexError("out of range")
            item = current.data
            previous.next = current.next
            return item

    def insert(self, position, item):
        if position < 0:
            raise IndexError("out of range")
        if position == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            index = 0
            while current is not None and index < position - 1:
                current = current.next
                index += 1
            if current is None:
                raise IndexError("out of range")
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node

    def slice(self, start, stop):
        if start < 0 or start > stop:
            raise ValueError("invalid values")
        if start == stop:
            return UnorderedList()  

        current = self.head
        index = 0
        while current is not None and index < start:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("out of range")

        new_list = UnorderedList()
        while current is not None and index < stop:
            new_list.append(current.data)
            current = current.next
            index += 1

        return new_list

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

