""" Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers """
from random import randint

randomlist = []
randomlist1 = []
matching_numbers = set()

while len(randomlist) <=10:
    randomlist.append(randint(1,10))
print(f'here\'s the first list of random numbers{randomlist}')

while len(randomlist1) <=10:
    randomlist1.append(randint(1,10))
print(f'here\'s the second list of random numbers{randomlist1}')

index = 0 #it didn't work with index 0

while index < len(randomlist):  
    if randomlist[index] in randomlist1:
        matching_numbers.update([randomlist[index]])
    index+=1

print(f"here are the unique numbers from both lists that are matching {matching_numbers}")