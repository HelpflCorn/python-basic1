# Task 3

# Fraction

# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й 
# обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу
# Fraction

 

# class Fraction:
#     pass

# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     y = Fraction(1, 4)
#     x + y == Fraction(3, 4)



from fractions import Fraction

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("can't be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("can't be zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)
    
    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)
    
    def __le__(self, other):
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)
    def __gt__(self, other):
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

fraction1 = Fraction(2,4)
fraction2 = Fraction(1,3)
print(fraction1<=fraction2)
print(fraction2==fraction1)
print(fraction1>=fraction2)
print(fraction2*fraction1)
print(fraction1/fraction2)
print(fraction2>fraction1)