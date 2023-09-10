# Task 1

# Practice asynchronous code

# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. Schedule the execution of this code using 
# asyncio.gather for a list of integers from 1 to 10. You need to get four lists of results from corresponding functions.

# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. Time the execution of both realizations, 
# explore the results, what realization is more effective, why did you get a result like this.


import asyncio

async def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return await calculate_fibonacci(n - 1) + await calculate_fibonacci(n - 2)

async def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * await calculate_factorial(n - 1)

async def calculate_square(n):
    return n * n

async def calculate_cubic(n):
    return n * n * n

async def main():
    input_number = 10

    fibonacci_result = await calculate_fibonacci(input_number)
    factorial_result = await calculate_factorial(input_number)
    square_result = await calculate_square(input_number)
    cubic_result = await calculate_cubic(input_number)

    print(f"Fibonacci({input_number}) = {fibonacci_result}")
    print(f"Factorial({input_number}) = {factorial_result}")
    print(f"Square({input_number}) = {square_result}")
    print(f"Cubic({input_number}) = {cubic_result}")

if __name__ == "__main__":
    asyncio.run(main())
