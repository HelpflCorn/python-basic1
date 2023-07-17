# Task 1

# Write a Python program to detect the number of local variables declared in a function.

def local_variables(n):
    print(f'this is the number of local variables in your function {n.__code__.co_nlocals}')

def sample_function(a,b,c):
    helo = a + " " + b + " " + c + " -  is what your input was"
    bye = a+c+" - this was the first and the last thing you wrote"
    print(f'{helo}, {bye}, why did you even write it?')

sample_function("potato", 'chips', "fries")

local_variables(sample_function)