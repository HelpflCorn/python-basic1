# Task 3

# Product Store

# Write a class Product that has three attributes:

# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods,
# in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
# classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store
# (30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers 
# (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case 
# raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, product_type, name, price):
        self.name = name
        self.price = price
        self.product_type = product_type
        
    def __str__(self):
        return f'{self.type} - {self.name} {self.price}'

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0
    
    def add_product(self, product, amount, premium):
        if not isinstance(amount, (float, int)) or amount <=0:
            raise ValueError("please add a proper amount, it should be a number and be bigger then 0")
        predefined_premium = Product(product.product_type, product.name, product.price * premium)
        self.products[product.name] = (predefined_premium, self.products.get(product.name, 0) + amount)
    
    def set_discount(self, identifier, discount_percentage, identifier_type='name'):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("discount percentage should be between 0 and 100.")
        
        self.products.update({ product_name: Product(product.product_type, product.name, product.price * (1 - discount_percentage / 100))
            for product_name, product in self.products.items()
            if (identifier_type == 'name' and product.name == identifier) or
               (identifier_type == 'type' and product.type == identifier) })
                
    def sell_product(self, product_name, how_many):
        if product_name not in self.products:
            raise ValueError("product not found.")
        
        product, available_quantity = self.products[product_name]
        
        if available_quantity < how_many:
            raise ValueError(f"Insufficient quantity of '{product_name}' in the store. Available: {available_quantity}")
        
        product.price /= 1.3
        self.income += product.price * how_many
        self.products[product_name] = (product, available_quantity - how_many)
        return product_name, self.products[product_name][1]
    
    def get_income(self):
        return self.income

    def get_all_products(self):
        return {name: amount for name, (_, amount) in self.products.items()}

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in the store.")
        product, amount = self.products[product_name]
        return product_name, amount

    def __str__(self):
        return "\n".join(str(product) for product, _ in self.products.values())
    
ben = Product("frog", "ben", 23)
store1 = ProductStore()
store1.add_product(ben, 1, 1.3)

print(store1.sell_product("ben", 1))