import itertools as it

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_numbers = it.count(0, 2)
print(even_numbers)
lst = list(next(even_numbers) for _ in range(5))
print(lst)

lst1 = list(zip(it.count(), ['a', 'b', 'c']))
print(lst1)


def print_iterable(iterable, end=None):
    for i in iterable:
        if end:
            print(i, end=end)
        else:
            print(i)


ones = it.repeat(1, 5)
print_iterable(ones, ' ')
print()

lst2 = list(map(pow, range(10), it.repeat(2)))
print(lst2)

# it.repeat() works faster than range()
# for _ in it.repeat(None, 10000):  # it works faster than range(10000)
    #  do something
# for _ in range(10000):
    #  compute

pos_neg_ones = it.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10)))
letters = it.cycle(['A', 'B', 'C'])
print(list(next(letters) for _ in range(10)))



