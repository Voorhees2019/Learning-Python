print(issubclass.__doc__)
print('--------------------------------------------------------')
help(issubclass)
print('--------------------------------------------------------')


class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


circle = Circle(10)
print(issubclass(Circle, Shape))
print(isinstance(circle, Circle))
print(isinstance(circle, Shape))
print()
print(callable(circle))  # object that defines __call__() is considered callable
print(callable(print))
print()

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))

print(dir(circle))
print(circle.__dict__)
print(Circle.__name__)
print(__name__)
print(type(circle))
print(id(circle))
print(repr(circle))

