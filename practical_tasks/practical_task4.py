"""1. 
Створіть програму для керування списком продуктів в інтернет-магазині. Кожен продукт може мати назву, ціну та кількість на складі. 
Реалізуйте можливість користувачу додавати нові продукти, оновлювати інформацію про продукти та виводити список доступних
 продуктів за певними критеріями (наприклад, за ціною або наявністю на складі).
 (потрібно використати ф-ю input(), щоб користувач міг вводити дані з консолі)"""


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
Напишіть програму для керування списком завдань. Кожне завдання може мати назву, опис, пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено"). Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.
"""
#tasks = {"Поїсти":{"Статус":"в очікуванні", "Приорітет":"Високий"}}
#print(tasks)
"""
3. 
Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 2-х чисел та вид математичної операції (+, -, *, /). Виведіть результат операції та продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.

4. 
Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку
["name", "surname", "domain"]
5. Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). Спробуйте використати вкладені списки

6.
Напишіть програму для керування студентськими оцінками. Реалізуйте можливість додавання оцінок, видалення оцінок, обчислення середнього балу студента та виведення списку студентів з їх оцінками.

7.
Створіть програму для управління замовленнями в ресторані. Використовуйте список (list) для зберігання замовлень, де кожне замовлення представлене як кортеж (tuple) з назвою страви і ціною. Реалізуйте можливість додавання нових замовлень, видалення замовлень і розрахунку загальної суми замовлення.

8.
У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. Надайте дані по наступним моментах:
- Які 3 продукти ваші клієнти купують найчастіше
- Які 3 продукти ваші клієнти купують найрідше?
- Скільки разів клієнти купували кожен з ваших продуктів?

9.
Напишіть програму для керування розкладом занять студентів. Використовуйте список (list) для зберігання інформації про заняття, де кожне заняття представлене як кортеж (tuple) з назвою предмету і часом проведення (це може бути як і день, так і конкретна година - вибирайте як вам зручніше). Реалізуйте можливість додавання нових занять, видалення занять і виведення розкладу занять за допомогою циклу for.

10.
Створіть програму для керування списком завдань. Використовуйте множину (set) для зберігання завдань, які потрібно виконати. Реалізуйте для користувача можливість додавання нових завдань, видалення завдань і перевірку, чи всі завдання виконані. (тобто користувач повинен мати змогу виконувати ці всі завдання через інпут з терміналу)

11.
Напишіть програму для керування списком книг у бібліотеці. Використовуйте словник (dict) для зберігання інформації про книги, де ключем буде назва книги, а значенням - автор книги. Реалізуйте можливість додавання нових книг, видалення книг і пошуку книг за автором. (тобто користувач повинен мати змогу робити ці всі речі через інпут з терміналу)

12.
Створіть програму для управління списком клієнтів у компанії. Використовуйте список (list) для зберігання інформації про кожного клієнта, де кожен клієнт представлений словником (dict) з ключами, такими як "ім'я", "посада" і "контактна інформація". Реалізуйте можливість додавання нових клієнтів, видалення клієнтів і пошуку клієнтів за певними критеріями (наприклад, за посадою). (ф-я input() і ввід користувача з терміналу)

13.
Розробіть програму для керування замовленнями в ресторані. Використовуйте список (list) для зберігання замовлень. Кожне замовлення може містити назву страви, кількість порцій та статус замовлення. Реалізуйте можливість додавання нових замовлень, видалення замовлень, оновлення статусу замовлення та виведення списку активних замовлень. (ф-я input() і ввід користувача з терміналу)

14.
Напишіть програму для управління списком проектів в IT-компанії. Використовуйте кортеж (tuple) для зберігання інформації про кожен проект, наприклад, назву проекту, замовника та строк виконання. Реалізуйте можливість додавання нових проектів, видалення проектів та виведення списку проектів, впорядкованих за строком виконання.
(ф-я input() і ввід користувача з терміналу)

15.
Створіть програму для управління списком студентів у навчальному закладі. Використовуйте множину (set) для зберігання імен студентів. Реалізуйте можливість додавання нових студентів, видалення студентів, перевірку присутності студента та виведення списку всіх студентів.
(ф-я input() і ввід користувача з терміналу)

16.
Розробіть програму для управління списком контактів. Використовуйте список (list) для зберігання контактів. Кожен контакт може містити ім'я, прізвище, номер телефону та електронну адресу. Реалізуйте можливість додавання нових контактів, видалення контактів, пошуку контактів за ім'ям або прізвищем та виведення списку всіх контактів. (ф-я input() і ввід користувача з терміналу)

17.
Напишіть програму для управління розкладом занять в навчальному закладі. Використовуйте словник (dict) для зберігання розкладу. Ключем буде день тижня, а значенням - список предметів на цей день. Реалізуйте можливість додавання нових занять, видалення занять та виведення розкладу на певний день. (ф-я input() і ввід користувача з терміналу)"""