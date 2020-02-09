import itertools as it

print(list(it.accumulate([1, 2, 3, 4, 5])))  # output: [1, 3, 6, 10, 15]
print(list(it.accumulate(['a', 'b', 'c', 'd'])))  # output: ['a', 'ab', 'abc', 'abcd']
# The first element that returns function accumulate is the first element in entry list (here is 1).
# Then accumulate returns the element, using two previous element and applying some function to them (addition is a
# default function)
print(list(it.accumulate([3, 1, 4, 2, 7, 3, 8, 5, 9], max)))  # returns [3, 3, 4, 4, 7, 7, 8, 8, 9]
print(list(it.chain('ABC', 'DEF')))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(list(it.chain.from_iterable(['ABC', 'DEF'])))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(list(it.chain([1, 2, 3], [4, 5, 6], [7, 8, 9])))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))  # [3, 4, 5]
print(list(it.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5])))  # [1, 2]
# if an element evaluate in False it.filterfalse returns in an output sequence
print(list(it.filterfalse(lambda x: x % 2 == 0, range(10))))  # [1, 3, 5, 7, 9]


def print_iterable(iterable, end=None):
    for i in iterable:
        if end:
            print(i, end=end)
        else:
            print(i)


iterable = iter([1, 2, 3])
print_iterable(iterable, ' ')
print('\niterable exhausted')
print_iterable(iterable, ' ')  # output: nothing because go through the iterator you can only once
print()

iterable1, iterable2 = it.tee([1, 2, 3, 4], 2)
print_iterable(iterable1, ' ')
print('\niterable exhausted')
print_iterable(iterable2, ' ')
print()


names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']
ratings = [2842, 2822, 2801, 2797, 2780]
for name, rating in zip(names, ratings):
    print(f'{name}:{rating}')
print(list(zip(names, ratings)))
print(dict(zip(names, ratings)))

names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri', 'Kramnik']
ratings = [2842, 2822, 2801, 2797, 2780]
print(dict(zip(names, ratings)))
print(dict(it.zip_longest(names, ratings, fillvalue=0)))


for key, group in it.groupby([1, 1, 1, 2, 2, 2, 3, 3]):
    print("{}:{}".format(key, list(group)))
print()
lst = [1, 2, 1, 2, 2, 3, 3, 2]
for key, group in it.groupby(sorted(lst)):
    print("{}:{}".format(key, list(group)))


forecast = [{'humidity': 20, 'temperature': 78, 'wind': 7},
            {'humidity': 50, 'temperature': 61, 'wind': 10},
            {'humidity': 100, 'temperature': 81, 'wind': 5},
            {'humidity': 90, 'temperature': 62, 'wind': 15},
            {'humidity': 20, 'temperature': 84, 'wind': 19},
            {'humidity': 0, 'temperature': 66, 'wind': 28},
            {'humidity': 100, 'temperature': 87, 'wind': 12},
            {'humidity': 0, 'temperature': 68, 'wind': 14},
            {'humidity': 90, 'temperature': 86, 'wind': 4},
            {'humidity': 50, 'temperature': 68, 'wind': 0}
            ]


def group_sorted(iterable, key=None):
    return it.groupby(sorted(iterable, key=key), key=key)


grouped_data = group_sorted(forecast, lambda x: x['humidity'])
for key, grp in grouped_data:
    print('{}:{}'.format(key, list(grp)))


even_numbers = it.count(0, 2)
print([x for x in range(20) if x % 2 == 0])
print(list(it.islice(even_numbers, 2, 10, 2)))  # islice(iterable, start_index, end_index, step_index)

even_numbers = it.count(0, 2)
print(list(it.islice(even_numbers, 4)))  # [0, 2, 4, 6]  takes only 4 elements






