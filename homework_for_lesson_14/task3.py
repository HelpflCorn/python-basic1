# Task 3

# Write a decorator "arg_rules" that validates arguments passed to the function.

# A decorator should take 3 arguments:

# max_length: 15

# type_: str

# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Argument '{arg}' is not of type '{type_.__name__}'")
                    return False
            for arg in args:
                if isinstance(arg, str) and len(arg) > max_length:
                    print(f"argument '{arg}' exceeds the maximum length of {max_length}")
                    return False
            for arg in args:
                if isinstance(arg, str):
                    for symbol in contains:
                        if symbol not in arg:
                            print(f"Argument '{arg}' does not contain the required symbol '{symbol}'")
                            return False

            return func(*args)

        return wrapper

    return decorator


# ```

# def arg_rules(type_: type, max_length: int, contains: list):

#     pass

 

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Vasyl Potapenko")
 

# assert create_slogan('johndoe05@gmail.com') is False

# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

