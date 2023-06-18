"""1.Вам потрібно запропонувати замовнику декілька варіантів створення електронних пошт для його працівників. 
Реалізуйте функціонал генерування пошт (з 3-ма варіантами, як приклад- taras.shevchenko@kobzar.com, 
tshev@kobzar.com і тд). 
* “kobzar.com” - це компанія, для якої ви реалізовуєте цей функціонал. 
 
Ви - злий касир в АТБ і продаєте алкогольні напої лише особам старше 18 років. Людям, старше 14 років і молодше 18 років,
 ви продаєте лише енергетичні напої. Всім решта - будь-що. 
Напишіть функціонал на пайтоні, який реалізує цей алгоритм.

3. 
Ви працюєте на проекті, який займається тим, що опрацьовує дані по платежах клієнтів від різних платіжних систем. 
Дані зберігаються в csv-файлах на Linux сервері. 
При перекидуванні даних на Windows сервер виявилось, 
що віндовс додає специфічні символи на позначення початку (“;”) і 
закінчення стрічки (“%”) з зашифрованим Transaction ID (було “yu7i9om0iymn”, стало “;yu7i9om0iymn%”). 
Це критичний баг для проекту. Реалізуйте механізм на пайтоні, який буде видаляти непотрібні символи з початку і 
кінця Transaction ID. 

4. Умова та ж сама, але тепер віндовс рандомно додає знак “&” в будь-яку позицію в стрічці 
Transaction ID (Було “yu7i9om0iymn”, стало “yu&7i9om&0iym&n”). 
Реалізуйте функціонал, який буде видаляти знак “&” зі стрічки"""

#task1
name = "Taras"
surname = "Shevchenko"
domain = "@kobzar.com"

option1 = name[0] + surname[0:5] + domain
option2 = name[0:2] + surname[0:2] + domain
option3 = name + surname + ("best_worker") + domain

print(option1, option2, option3)

#task2

message1 = "Купуй що завгодно"
message2 = "Вам можна тільки енергетик"
message3 = "Попий кока-колу"

age = 21

if age < 14:
    print(message3)
elif age > 14 and age <18:
    print(message2)
else: print(message1)

#task3
transaction_id = (";yu7i9om0iymn%")
transaction_id_copy = transaction_id.replace(";", "").replace("%", "")
print(transaction_id_copy)

#task4
transaction_id_bugged = ("yu&7i9&&om&&0iy&m&n")
for i in transaction_id_bugged:
    if i == "&":
        transaction_id_bugged = transaction_id_bugged.replace("&", "")
print(transaction_id_bugged)




