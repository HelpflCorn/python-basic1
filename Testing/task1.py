import unittest
import threading

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname}, I am always saying truth about my age and I am {self.age} years old')
        

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Yurii", "Tkach", 18)
        self.person2 = Person("Nichoho_sobi", "Otakoi", 95)

    def test_init(self):
        self.assertEqual(self.person1.firstname, "Yurii")
        self.assertEqual(self.person1.lastname, "Tkach")
        self.assertEqual(self.person1.age, 18)

        self.assertEqual(self.person2.firstname, "Nichoho_sobi")
        self.assertEqual(self.person2.lastname, "Otakoi")
        self.assertEqual(self.person2.age, 95)


if __name__ == "__main__":
    unittest.main()