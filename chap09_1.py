class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return self.__operate(other, '+')

    def __sub__(self, other):
        return self.__operate(other, '-')

    def __mul__(self, other):
        return self.__operate(other, '*')

    def __eq__(self, other):
        if isinstance(other, Point):
            x = other.x == self.x
            y = other.y == self.y
            z = other.z == self.z
            return x and y and z
        else:
            return False

    def __rmult__(self, other):
        if isinstance(other, Point):
            x = other.x * self.x
            y = other.y * self.y
            z = other.z * self.z
        elif isinstance(other, ['int', 'float']):
            x = other * self.x
            y = other * self.y
            z = other * self.z
        else:
            return NotImplemented

        return Point(x=x, y=y, z=z)

    def __operate(self, other, op):
        if isinstance(other, Point):
            x = eval(f'self.x {op} other.x')
            y = eval(f'self.y {op} other.y')
            z = eval(f'self.z {op} other.z')
        elif isinstance(other, ['int', 'float']):
            x = eval(f'self.x {op} other')
            y = eval(f'self.y {op} other')
            z = eval(f'self.z {op} other')
        else:
            return NotImplemented

        return Point(x=x, y=y, z=z)
