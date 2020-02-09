import math


class Shape:

    def __init__(self):
        print('Shape created')

    def draw(self):
        raise NotImplementedError("Can't instantiate an abstract class")

    def area(self):
        raise NotImplementedError("Can't instantiate an abstract class")

    def perimeter(self):
        raise NotImplementedError("Can't instantiate an abstract class")


class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height
        print('Rectangle created')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height)*2

    def draw(self):
        print(f'Drawing rectangle with width={self.width} and height={self.height}')


rect = Rectangle(10, 15)
print(rect.area())
rect.draw()
print('------------------------------------------')


class Triangle(Shape):

    def __init__(self, a, b, c):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        print('Triangle created')

    def draw(self):
        print(f'Drawing triangle with sides: {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def perimeter(self):
        return self.a+self.b+self.c


triangle = Triangle(10, 10, 10)
triangle.draw()
print(triangle.area())
print(triangle.perimeter())
print('------------------------------------------')

for shape in [rect, triangle]:
    shape.draw()

