# Write a decorator that prints a function with arguments passed to it.

# NOTE! It should print the function, not the result of its execution!

# For example:

#  "add called with 4, 5"

# ```

def logger(func):
    def wrapper(*args):
       print(f'{func.__name__} has called the following arguments {args}')
       return func(*args)
    return wrapper

 

@logger
def add(x, y):
    return x + y
add(3,7)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(square_all(6,3,2))