from random import randint
x = randint(1, 10)
y = input("Try to guess a number between 1 and 10: ")
if x == int(y):
    print("Yaay, you've guessed correctly!")
else:
    print(f"Well, actually this time the number was {x}")
    