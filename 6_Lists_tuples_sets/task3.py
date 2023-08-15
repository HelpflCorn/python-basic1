""" Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration """

""" list1 = [i for i in range(1,101, 7) if i%5!=0] #without a while loop """

list2 = list(range(1,100))
list3 = []
index = 0

while index<len(list2):
    if list2[index]%7==0 and list2[index]%5!=0:
        list3.append(list2[index])
    index+=1
print(list3)