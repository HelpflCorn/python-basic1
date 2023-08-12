""" Task 1
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values.  """
#

a = input("Write something here: ")
b = a.lower().replace(",","")
y = b.split()
z = {word:y.count(word) for word in y} #.count to return the number of times the word is used

""" for i in y:
    if i in z:
        z[i]+=1
    else:
        z[i]=1 """

print(z)