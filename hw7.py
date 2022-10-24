# Є дікт, невідомого наповнення. В дікті присутні ключі, занченням для яких є дікти невідомого наповнення в яких
# можуть бути аналогічні вкладені дікти. Напишіть функцію, яка дістане всі ключі зі значеннями не-діктами з усіх рівнів
# вкладення, помістить на один рівень в окремий дікт і поверне цей дікт.
# Напишіть докстрінг для цієї функці.

my_store = {
    'fruits':
        {
            'oranges': 25,
            'bananas': 34,
            'kiwi': 50,
            'vegetables':
                {
                    'potatoes': 56,
                    'tomatoes': 89,
                    'cucumbers': 25,
                    'beverages':
                        {
                            'water': 78,
                            'juice': 95
                        }

                }
        }

}


def get_keys(elem):
    """
    Function get_keys converts a multilevel dict(my_store) to a single-level one.
    """
    level_one = {}
    for key, value in elem.items():
        if type(value) is dict:
            level_one.update(get_keys(value))
        else:
            level_one[key] = value
    return level_one


print(get_keys(my_store))
