import random
import time


def game_decorator(func):
    """
    Функція декоратор, яка рахує та виводить час виконання функції.

    """
    def wrapper():
        start_game = time.time()
        result = func()
        end_game = time.time()
        game_duration = end_game - start_game
        print('Гра тривала: ', game_duration, 'сек.')
        return result
    return wrapper


@game_decorator
def program_game():
    """
    Дана функція є основою гри "Вгадай число". Функція запитує число від 1 до 100 у гравця та порівнює введене значення
    із загаданим програмою.

    """
    random_number = random.randint(1, 100)
    while True:
        user_number = int(input('Введіть число: '))
        if user_number == random_number:
            print('Поздоровляємо!')
            break
        elif abs(user_number - random_number) > 10:
            print('Холодно')
        elif 5 <= abs(user_number - random_number) <= 10:
            print('Тепло')
        elif 1 <= abs(user_number - random_number) <= 4:
            print('Гаряче')
    user_answer = input('Ви вгадали число! Бажаєте повторити гру? (вкажіть словом "так" чи "ні"): ')
    if user_answer in ('ТАК', 'так', 'Так'):
        program_game()
    else:
        print('Гру закінчено!')
