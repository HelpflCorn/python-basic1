"""1. 
Створіть програму для керування списком продуктів в інтернет-магазині. Кожен продукт може мати назву, ціну та кількість на складі. 
Реалізуйте можливість користувачу додавати нові продукти, оновлювати інформацію про продукти та виводити список доступних
 продуктів за певними критеріями (наприклад, за ціною або наявністю на складі).
 (потрібно використати ф-ю input(), щоб користувач міг вводити дані з консолі)
"""

product = {"product1":{"price":1, "quantity":1}}
print("\n")
print("Here is the current list of products: ", product)
print("\n")
a = input("Do you want to add or update anything? y/n ")
if a == "n":
    print("Okay, thank you!")
elif a != "n" and a != "y":
    print("Please insert y or n")
else:
    x = input("Please insert product name: ")
    y = input("Please insert product property \"price:" )
    i = input("Please insert product property \"quantity: ")

    product.update({x:{"price":int(y), "quantity":int(i)}})
    print("Here's the new list of products", product) 
"""
2. 
Напишіть програму для керування списком завдань. Кожне завдання може мати назву, опис, 
пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено"). 
Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.
"""
tasks = {"поїсти":{"Статус":"в очікуванні", "Приорітет":"високий"}}
print(f"Here\'s the list of your tasks {tasks}")
x = input("Please insert \"y\" if you'd want to update any of the tasks or add a new one")
if x == "y":
    dict_1 = input("Please enter which tasks you'd like to update")
    dict_2 = input("Please enter what status you'd like to set for this task: 1,2,3")
    dict_3 = input("Please enter the priority for this task:")
    tasks.update({dict_1.lower():{"Статус":dict_2.lower(), "Приорітет":dict_3.lower()}})
    print(f"Here's the updated list {tasks}")
if x != "y":
    print(f"Okay, this is the current status of your tasks {tasks}")


"""
3. 
Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 
2-х чисел та вид математичної операції (+, -, *, /). 
Виведіть результат операції та продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.
"""
x = input("If you want to stop using the program - write \"q\" here or at any moment further, to continue write \"okay\":")
while x != "q":
    first = input("Please insert the first number:" )
    if first.lower() == "q":
        print("okay, see you later!")
        break
    second = input("Please insert the second number" )
    if first.lower() == "no":
        print("okay, see you later!")
        break
    operator = input("Please select the operator: +, -, *, /:" )
    if operator.lower == "no":
        print("okay, see you later")
    if operator == "+":
        print(int(first) + int(second))
    if operator == "-":
        print(int(first) - int(second))
    if operator == "*":
        print(int(first) * int(second))
    if operator == "/":
        print(int(first) / int(second))
print("okay, bye!")
    

""" 4. 
Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку
["name", "surname", "domain"] """

list1 = ["Mykhailo", "007", "@RzhyshchivDynamics.com"]
print(list1[0]+list1[1]+list1[2])


""" 5. Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). 
Спробуйте використати вкладені списки """

list2 = [["Mykhailo","007", "@RzhyshchivDynamics.com"], ["Serhii","Nusk", "@RzhyshchivDynamics.com"], ["Vasyl","Vezos", "@RzhyshchivDynamics.com"], ["Petro","Oage", "@RzhyshchivDynamics.com"], ["Taras","Vrin", "@RzhyshchivDynamics.com"]]
print(list2[0][0] + list2[0][1] + list2[0][2])
print(list2[1][0] + list2[1][1] + list2[1][2])
print(list2[2][0] + list2[2][1] + list2[2][2])
"""
6.
Напишіть програму для керування студентськими оцінками. 
Реалізуйте можливість додавання оцінок, видалення оцінок, обчислення середнього балу студента та виведення списку студентів з 
їх оцінками.
"""
#
from statistics import mean

name1marks = [5, 8, 10, 12, 8]
name2marks = [7, 4, 8, 10]
marks = {'Taras Shevchenko':name1marks, 'Valerian Pidmohylnyi':name2marks}
print(marks)
a = input("If you want to add another mark to one of the existing students press \"y\", press \"n\" if you want to add a new student and \"a\' to see the average scores")

if a =="y":
    b = input("Select the existing student whose mark you'd like to update")
    c = input("Select the mark that you would like to add: ")
    if b == "Taras Shevchenko":
        name1marks.append(c)
    if b == "Valerian Pidmohylnyi":
        name2marks.append(c)
    print(marks)
if a =="n":
    i = input("Would you like to add a new student to the list? y/n")
    if i == "y":
        o = input("Please insert a student name: ")
        p = input("Please insert the mark or marks that you'd like to give: ")
        name3marks=[]
        name3marks.append(int(p))
        marks.update({o:[int(p)]})
        print(marks)
if a=="a":
    q = input("Please insert the student name for whom you'd like to see the average scores: ")
    if q == "Taras Shevchenko":
        print(mean(marks["Taras Shevchenko"]))
    if q == 'Valerian Pidmohylnyi':
        print(mean(marks["Valerian Pidmohylnyi"]))
    elif q != "Valerian Pidmohylnyi" and q != "Taras Shevchenko":
        print("There is no such student")
    #cannot add an average for a new student if he hasn't been defined, don't know what to do
elif a !="y" and a !="n"and a != "a":
     print(f"You shoud insert the a, y or n, the current list of marks is {marks}")
    
    

""" 7.
Створіть програму для управління замовленнями в ресторані.
Використовуйте список (list) для зберігання замовлень, де кожне замовлення представлене як кортеж (tuple) з 
назвою страви і ціною. Реалізуйте можливість додавання нових замовлень, 
видалення замовлень і розрахунку загальної суми замовлення.

8.
У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. 
Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. 
Надайте дані по наступним моментах:
- Які 3 продукти ваші клієнти купують найчастіше
- Які 3 продукти ваші клієнти купують найрідше?
- Скільки разів клієнти купували кожен з ваших продуктів?

9.
Напишіть програму для керування розкладом занять студентів. 
Використовуйте список (list) для зберігання інформації про заняття, де кожне заняття 
представлене як кортеж (tuple) з назвою предмету і часом проведення (це може бути як і день, 
так і конкретна година - вибирайте як вам зручніше). Реалізуйте можливість додавання нових занять,
видалення занять і виведення розкладу занять за допомогою циклу for.

10.
Створіть програму для керування списком завдань. Використовуйте множину (set) для зберігання завдань, 
які потрібно виконати. Реалізуйте для користувача можливість додавання нових завдань, видалення завдань 
і перевірку, чи всі завдання виконані. (тобто користувач повинен мати змогу виконувати ці всі завдання через
інпут з терміналу)

11.
Напишіть програму для керування списком книг у бібліотеці. 
Використовуйте словник (dict) для зберігання інформації про книги, де ключем буде назва книги, а
значенням - автор книги. Реалізуйте можливість додавання нових книг, видалення книг і пошуку книг за автором. 
(тобто користувач повинен мати змогу робити ці всі речі через інпут з терміналу)

12.
Створіть програму для управління списком клієнтів у компанії. Використовуйте список (list) для зберігання 
інформації про кожного клієнта, де кожен клієнт представлений словником (dict) з ключами, такими як "ім'я", 
"посада" і "контактна інформація". Реалізуйте можливість додавання нових клієнтів, 
видалення клієнтів і пошуку клієнтів за певними критеріями (наприклад, за посадою). (ф-я input() і
ввід користувача з терміналу)

13.
Розробіть програму для керування замовленнями в ресторані. 
Використовуйте список (list) для зберігання замовлень. 
Кожне замовлення може містити назву страви, кількість порцій та статус замовлення. 
Реалізуйте можливість додавання нових замовлень, видалення замовлень, 
оновлення статусу замовлення та виведення списку активних замовлень. (ф-я input() і ввід користувача з терміналу)

14.
Напишіть програму для управління списком проектів в IT-компанії. Використовуйте кортеж (tuple) для зберігання
інформації про кожен проект, наприклад, назву проекту, замовника та строк виконання. 
Реалізуйте можливість додавання нових проектів, видалення проектів та виведення списку проектів, 
впорядкованих за строком виконання.
(ф-я input() і ввід користувача з терміналу)

15.
Створіть програму для управління списком студентів у навчальному закладі. Використовуйте множину (set) для 
зберігання імен студентів. Реалізуйте можливість додавання нових студентів, видалення студентів, 
перевірку присутності студента та виведення списку всіх студентів.
(ф-я input() і ввід користувача з терміналу)

16.
Розробіть програму для управління списком контактів. Використовуйте список (list) для зберігання контактів.
Кожен контакт може містити ім'я, прізвище, номер телефону та електронну адресу. 
Реалізуйте можливість додавання нових контактів, видалення контактів, пошуку контактів за ім'ям або 
прізвищем та виведення списку всіх контактів. (ф-я input() і ввід користувача з терміналу)

17.
Напишіть програму для управління розкладом занять в навчальному закладі. 
Використовуйте словник (dict) для зберігання розкладу. Ключем буде день тижня, а значенням - 
список предметів на цей день. Реалізуйте можливість додавання нових занять, 
видалення занять та виведення розкладу на певний день. (ф-я input() і ввід користувача з терміналу) """