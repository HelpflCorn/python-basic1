# Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its 
# functionality to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for 
# saving messages to file


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')