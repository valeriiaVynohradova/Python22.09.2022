# Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран кількість слів,
# які містять дві голосні літери підряд.

some_string = input('Enter your text: ').split()
vowels = set('aeiouAEUIO')
word_count = 0
for word in some_string:
    vowel_letter = 0
    for letter in word:
        if letter in vowels:
            vowel_letter += 1
        else:
            vowel_letter = 0
        if vowel_letter == 2:
            word_count += 1
            break
print(f'Your string contains {word_count} words with 2 in a row vowel letter.')

# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви
# магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

lower_limit = input('Select min price:')
upper_limit = input('Select max price:')
some_dict = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
             "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
while True:
    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
    except ValueError:
        print('Please, enter correct data')
        continue
    break
store_list = list()
for store in some_dict.items():
    if lower_limit < store[1] < upper_limit:
        store_list.append(store[0])
print('match: ', str(store_list).replace('[', '').replace(']', ''))
