# функцію is_string_capitalized потрібно дописати (в тому числі докстрінги) - очікування - прохід тестів
# напишіть функцію, яка перевірить, чи дане число є парним чи непарним(коментар з коду видаліть) ТА ПОКРИЙТЕ ЇЇ ТЕСТАМИ

def is_string_capitalized(string):
    """
        Function check if the given string is capitalised
        Args:
            string: string to check on capitalised

        Returns:
            bool: True|False
        """

    if string == '':
        return True
    elif string.isalnum():
        return True
    elif string[0].isupper() and string[1:].islower() is True:
        return True
    elif string[0].isupper() and string[1:].islower() is False:
        return False
    else:
        return False


def odd_or_even(number):
    """
    Function check if the given number is odd or even
    :param number: number to check if it odd or even
    :return: True|False
    """
    if number % 2 == 0:
        return True
    else:
        return False
