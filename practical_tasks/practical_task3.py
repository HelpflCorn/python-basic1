"""1
Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 2-х чисел та вид математичної 
операції (+, -, *, /). 
Виведіть результат операції та продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.

2
Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку
["name", "surname", "domain"]

3
Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). 
Спробуйте використати вкладені списки

4
Створіть програму для керування списком продуктів в інтернет-магазині. 
Кожен продукт може мати назву, ціну та кількість на складі. 
Реалізуйте можливість користувачу додавати нові продукти, оновлювати інформацію 
про продукти та виводити список доступних продуктів за певними критеріями (наприклад, за ціною або 
наявністю на складі).

5
Напишіть програму для керування списком завдань. Кожне завдання може мати назву, 
опис, пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено"). 
Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.

6
Простіший спосіб оновити дані в дікті замість функції update:
my_dict[«first_key»] = "new_value"

7
my_dict["first_key"]["price"] = "new_value"""
#

#Task1

first = int(input("Please insert the first number:" ))
second = int(input("Please insert the second number" ))
operator = input("Please select the operator: +, -, *, /:" )
if operator == "+":
    print(int(first) + int(second))
if operator == "-":
    print(int(first) - int(second))
if operator == "*":
    print(int(first) * int(second))
if operator == "/":
    print(int(first) / int(second))

#Task 2

list1 = ["Mykhailo", "007", "@sraka.com"]
print(list1[0]+list1[1]+list1[2])