iterable = [1, 2, 3]
iterator = iter(iterable)  # будет вызван метод __iter__()
print(type(iterator))
print(next(iterator))  # будет вызван метод __next__()
print(next(iterator))
print(next(iterator))




