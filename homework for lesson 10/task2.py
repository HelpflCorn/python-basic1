# Task 2

# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero 
# (cannot divide by zero).    


print("this program will divide the square first number by the second number")
print('\n')
a = input("Enter the first number: ")
b = input("Enter the second number: ")

def square_and_divide(a, b):
    try:
        a = int(a)
        b = int(b)
        result = (a*a)/b
        print(f'this is the result: {int(result)}')
    except: 
        ZeroDivisionError
        print("most probably you've tried to divide by zero, it doesn't work this way")
        ValueError
        print("Or you've entered something that is not a number")

square_and_divide(a=a, b=b)