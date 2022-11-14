from homework9 import hw9_library

assert hw9_library.is_string_capitalized('My name is David') is False
assert hw9_library.is_string_capitalized('I love playing') is True
assert hw9_library.is_string_capitalized('') is True
assert hw9_library.is_string_capitalized('565656') is True

assert hw9_library.odd_or_even(57) is False
assert hw9_library.odd_or_even(4.0) is True
assert hw9_library.odd_or_even(4) is True
assert hw9_library.odd_or_even(5) is False
assert hw9_library.odd_or_even(0) is True
