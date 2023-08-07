# Exercise 1: Online Store Inventory Management
# Create a class hierarchy to represent an online store's inventory management system. 
# Start with a base class called Product and include attributes such as name, price, and quantity. 
# Create subclasses for specific types of products, such as Electronics, Clothing, and Books. 
# Each subclass should have additional attributes and methods specific to the type of product. 
# Implement methods for adding new products, updating quantities, and calculating total inventory value.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")

class Electronics(Product):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand
        
class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

class Books(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
        
class InventoryChanges:
    def __init__(self):
        self.inventory = []
        
    def new_product(self, product):
        self.inventory.append(product)
        print(f'{product} was added to inventory')
            
    def update_quantity(self, name, quantity):
        for i in self.inventory:
            if i == name:
                quantity = quantity
            
            
    
    

    
# Exercise 2: Employee Management System
# Design a class hierarchy to represent an employee management system for a company. 
# Start with a base class called Employee and include attributes such as name, position, and salary. 
# Create subclasses for different types of employees, such as Manager, Developer, and Salesperson. 
# Each subclass should have additional attributes and methods specific to the role of the employee. 
# Implement methods for calculating salary bonuses, tracking attendance, and generating employee reports.

# Exercise 3: Library Management System
# Create a class hierarchy to represent a library management system. 
# Start with a base class called LibraryItem and include attributes such as title, author, and available. 
# Create subclasses for specific types of items, such as Book, DVD, and Magazine. 
# Each subclass should have additional attributes and methods specific to the type of item. 
# Implement methods for checking out and returning items, generating overdue item reports, and 
# searching for items by title or author.

# Exercise 4: Banking System
# Design a class hierarchy to represent a banking system. Start with a base class called Account and include attributes 
# such as account_number, balance, and interest_rate. Create subclasses for different types of accounts, 
# such as SavingsAccount, CheckingAccount, and LoanAccount. 
# Each subclass should have additional attributes and methods specific to the type of account. 
# Implement methods for depositing and withdrawing funds, calculating interest, and generating account statements.

# Exercise 5: Flight Booking System
# Create a class hierarchy to represent a flight booking system for an airline. 
# Start with a base class called Flight and include attributes such as flight_number, departure, and arrival. 
# Create subclasses for different types of flights, such as DomesticFlight and InternationalFlight. 
# Each subclass should have additional attributes and methods specific to the type of flight. 
# Implement methods for booking seats, checking flight availability, and generating passenger manifests.