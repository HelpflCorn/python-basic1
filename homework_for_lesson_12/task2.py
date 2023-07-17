# Task 2

# Write a Python program to access a function inside a function 
# (Tips: use function, which returns another function)

def outer():
    def inner():
        print('hi there!')
    return inner()

outer()