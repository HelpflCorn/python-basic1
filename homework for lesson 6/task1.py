""" Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers """

from random import randint

randlist = []

while len(randlist) <10:
    randlist.append(randint(1,10))


max_number = 0
index = 1

while index < len(randlist):
    if randlist[index] >= max_number:
        max_number = randlist[index]
    index+=1

print(randlist)
print(max_number)