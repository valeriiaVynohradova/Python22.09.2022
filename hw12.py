# Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
# перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3
# print(str(triangle1))
# > (1,0 -- 5,9 -- 3,3)

class Point:
    _x = 0
    _y = 0

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError
        self._y = new_y


class Triangle:
    _a = None
    _b = None
    _c = None

    def __init__(self, init_a, init_b, init_c):
        self.a = init_a
        self.b = init_b
        self.c = init_c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, Point):
            raise TypeError
        self._a = new_a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, Point):
            raise TypeError
        self._b = new_b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, new_c):
        if not isinstance(new_c, Point):
            raise TypeError
        self._c = new_c

    @property
    def triangle_square(self):
        """
        Розраховуємо довжину сторін AB, BC, AC
        """
        ab_x = (self._a.x - self._b.x) ** 2
        ab_y = (self._a.y - self._b.y) ** 2
        length_ab = (ab_x + ab_y) ** 0.5

        bc_x = (self._b.x - self._c.x) ** 2
        bc_y = (self._b.y - self._c.y) ** 2
        length_bc = (bc_x + bc_y) ** 0.5

        ac_x = (self._a.x - self._c.x) ** 2
        ac_y = (self._a.y - self._c.y) ** 2
        length_ac = (ac_x + ac_y) ** 0.5
        """
        Розраховуємо половину периметра
        """
        p = (length_ab + length_bc + length_ac) / 2
        """
        Розраховуємо площу за формулою Герона
        """
        triangle_square = (p * (p - length_ab) * (p - length_bc) * (p - length_ac)) ** 0.5

        return triangle_square

    def __eq__(self, other):
        return self.triangle_square == other.triangle_square

    def __ne__(self, other):
        return self.triangle_square != other.triangle_square

    def __lt__(self, other):
        return self.triangle_square < other.triangle_square

    def __le__(self, other):
        return self.triangle_square <= other.triangle_square

    def __gt__(self, other):
        return self.triangle_square > other.triangle_square

    def __ge__(self, other):
        return self.triangle_square >= other.triangle_square

    def __str__(self):
        return f'{self.a.x}, {self.a.y}, {self.b.x}, {self.b.y}, {self.c.x}, {self.c.y}'


a = Point(0, 5)
b = Point(6, 5)
c = Point(6, 0)
d = Point(2, 0)

triangle1 = Triangle(a, b, c)
triangle2 = Triangle(d, b, c)
print(f'The square of the triangle 1 is {triangle1.triangle_square}')
print(f'The square of the triangle 2 is {triangle2.triangle_square}')

print(str(triangle1))
print(str(triangle2))


def comparison(value1, value2):
    """
    Дана функція порівнює площі трикутників за координатами
    """
    if value1 == value2:
        print('The square of the triangle 1 is equal to triangle 2')
    else:
        print('The square of the triangle 1 is not equal to triangle 2')
    if value1 >= value2:
        print('The square of the triangle 1 is greater than or equal than triangle 2 ')
    else:
        print('The square of the triangle 1 is less than or equal than triangle 2 ')
    if value1 > value2:
        print('The square of the triangle 1 is greater than triangle 2')
    else:
        print('The square of the triangle 1 is less than triangle 2')


comparison(value1=triangle1, value2=triangle2)
