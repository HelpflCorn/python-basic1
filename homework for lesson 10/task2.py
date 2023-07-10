
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