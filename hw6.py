# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def get_float(arg):
    try:
        arg = float(arg)
        return arg
    except:
        return 0


user_argument = input('Enter your argument: ')
result = get_float(user_argument)
print(result)

# 2. Напишіть функцію, що приймає два аргументи. Функція повинна:
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів


def my_func(first_arg, second_arg):
    if (type(first_arg) == int or type(first_arg) == float) and (type(second_arg == int or type(second_arg) == float)):
        return first_arg * second_arg
    elif type(first_arg) == str and type(second_arg) == str:
        return first_arg + second_arg
    else:
        return first_arg, second_arg

# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача
# (1 - рік, 22 - роки, 35 - років і тд...).
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"


def correct_forms(age):
    age_endings = ('рік', 'років', 'роки')
    if age % 100 in (11, 12, 13, 14):
        return age_endings[1]
    elif age % 10 == 1:
        return age_endings[0]
    elif age % 10 in (2, 3, 4):
        return age_endings[2]
    else:
        return age_endings[1]


def condition_check(age, age_endings):
    if '7' in str(age):
        print(f'Вам {age} {age_endings}, вам пощастить')
    elif age < 7:
        print(f'Тобі ж {age} {age_endings}! Де твої батьки?')
    elif age < 16:
        print(f'Тобі лише {age} {age_endings}, а це  фільм для дорослих!')
    elif age > 65:
        print(f'Вам {age} {age_endings}? Покажіть пенсійне посвідчення!')
    else:
        print(f'Незважаючи на те, що вам {age} {age_endings} , білетів всеодно нема!')


def get_age():
    user_age = input('Введіть свій вік: ')
    if user_age.isdigit() and int(user_age) > 0:
        user_age = int(user_age)
        forms = correct_forms(age=user_age)
        condition_check(age=user_age, age_endings=forms)
    else:
        print('Введені некоректні дані. Спробуйте знову! ')


get_age()
