""" 
Task 4
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1, """

from datetime import date
list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dict1 = {i+1:day for i, day in enumerate(list)}
dict2 = {day:i+1 for i, day in enumerate(list)}
print(dict1)
print(dict2)