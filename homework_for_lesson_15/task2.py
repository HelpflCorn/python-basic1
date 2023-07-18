# Task 2

# Doggy age

# Create a class Dog with class attribute 'age_factor' equals to 7. 
# Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age 
# in human equivalent.

class Dog:
    age_factor = 7
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def human_age(self):
        print(f"The dog's name is {self.name} and the age is {self.age}, which in human years is {self.age*Dog.age_factor}")
        
dog1 = Dog("Laika", 3)
dog1.human_age()