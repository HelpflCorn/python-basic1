# Task 1

# School

# Make a class structure in python representing people at school. Make a base class called Person, 
# a class called Student, and another one called Teacher. Try to find as many methods and attributes 
# as you can which belong to different classes, and keep in mind which are common and which are not. 
# For example, the name should be a Person attribute, while salary should only be available to the 
# teacher. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def basic_info(self):
        print(f"this person's name is {self.name}, they are {self.age} years old")

class Student(Person):
    def __init__(self, name, age, id, marks):
        super().__init__(name,age)
        self.marks = marks

    def study(self, subject):
        print(f'{self.name} is studying {subject}')

    
class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teaching(self, subject):
        print(f"{self.name} is teaching {subject}")
    def show_salary(self):
        print(f"this person receives {self.salary} per month")

teacher1 = Teacher("Petro", 12, "one potato")
teacher1.show_salary()
student1 = Student("Vasyl", 35, 263, "only bad ones")
student1.basic_info()
student1.study("Advanced sofa-sitting")