# Mathematician

# Implement a class Mathematician which is a helper class for doing math operations on lists

# The class doesn't take any attributes and only has methods:

# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
# '''

# class Mathematician:

#     pass

 

# m = Mathematician()

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# '''

class Mathematician:

    def square_nums(self, *args):
        return [num**2 for num in args]

    def remove_positives(self, *args):
        print(f'these are your numbers {args}')
        return(f"these were the negative numbers to remove {[num for num in args if num < 0]}")

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def filter_leaps(self, *years):
        return [year for year in years if self.is_leap_year(year)]
    
math1 = Mathematician()
print(math1.square_nums(5,7,2,56))
print(math1.remove_positives(4,0,-3,5))
print(math1.is_leap_year(2000))
print(math1.filter_leaps(200,12, 10000))