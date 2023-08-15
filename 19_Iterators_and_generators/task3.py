# Task 3

# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


iterable1 = CustomIterable([1, 5, 2, 9992492, 5])

for item in iterable1:
    print(item)