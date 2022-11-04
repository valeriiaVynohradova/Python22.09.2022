# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    main_colour = None
    brand = None
    weight = None

    def __init__(self, main_colour, brand, weight):
        self.main_colour = main_colour
        self.brand = brand
        self.weight = weight

    def print_text(self):
        return f'The colour of {self.brand} is {self.main_colour}, weight is {self.weight} kg.'


class Car(Vehicle):
    vehicle_capacity = None

    def print_text(self):
        return f'The colour of {self.brand} is {self.main_colour}, weight is {self.weight} kg and vehicle capacity' \
               f' is {self.vehicle_capacity} persons.'


class Plane(Vehicle):
    number_of_engines = None

    def print_text(self):
        return f'The colour of {self.brand} is {self.main_colour}, weight is {self.weight} kg and number of windows ' \
               f'is {self.number_of_engines}.'


class Ship(Vehicle):
    top_speed = None

    def print_text(self):
        return f'The colour of {self.brand} is {self.main_colour}, weight is {self.weight} kg and speed is' \
               f' {self.top_speed} knots.'


Porsche = Car('violet', 'Porsche', 1985)
Porsche.vehicle_capacity = 5

Mriya = Plane('white', 'Mriya', 285000)
Mriya.number_of_engines = 6

Titanik = Ship('black', 'Titanik', 52310000)
Titanik.top_speed = 23

print(Porsche.print_text())
print(Mriya.print_text())
print(Titanik.print_text())
