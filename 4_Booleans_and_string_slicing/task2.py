"""Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation."""

#task
phone_number = ("0963564678")
if len(phone_number) == 10 and phone_number.isnumeric() == True:
    print("This is a phone number")
if len(phone_number) != 10:
    print("This doesn't look like a phone number, please check if your number has 10 digits")
if phone_number.isnumeric() != True:
    print("The phone number should only consist of numbers, that's why it's called \"NUMBER\"")