""" List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` 
is corresponding to `i` squared. """
#
list1 = [(i, i**2) for i in range(11)]

print(list1)