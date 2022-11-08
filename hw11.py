# 1. Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти
# класу int або float
# 2. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку
# даних, аналогічно до класу Line. Визначет атрибут, що містить площу трикутника (за допомогою property). Для обчислень
# можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
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
