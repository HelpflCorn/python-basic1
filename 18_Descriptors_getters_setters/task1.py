
# Task 1

# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, 
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is 
# a valid email string.

import re

class EmailValidator:
    def __init__(self, email):
        self.email = email
        self._validate_format()

    def _validate_format(self):
        regex = r'^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$'
        if re.match(regex, self.email):
            return 'the format is matching'
        return "there's something wrong, please try again"

    

email1 = EmailValidator("helpfulcorn@gmail.com")
print(email1._validate_format())
email2 = EmailValidator("poplavskyi..super!!!!@knukim.edu.ua")
print(email2._validate_format())