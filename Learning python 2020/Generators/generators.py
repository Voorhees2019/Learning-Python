import random
import itertools


def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


for r in randoms(10, 100, 5):
    print(r)

rand_sequence = randoms(1, 10, 10)
print(rand_sequence)  # <generator object randoms at 0x01032AF0>

for i in rand_sequence:
    print(i, end=' ')
print()
# по объекту генератора можно пройтись только один раз
# этот код ничего не выведет
for i in rand_sequence:
    print(i)
# поэтому обычно объект генератора запихивают в список для многоразового использования
seq = list(randoms(1, 10, 5))
print(seq)
print('-------------------------------------------')
rand_sequence = randoms(1, 10, 10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)
print('-------------------------------------------')


def randoms(min, max):
    while True:
        yield random.randint(min, max)


rand_sequence = randoms(1, 10000)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


def read_line_by_line(file):
    """Lazy function (generator) to read a file line by line."""
    while True:
        line = file.readline()
        if not line:
            break
        else:
            yield line


some_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eros quis dolor bibendum euismod. 
Etiam eleifend, tellus nec fringilla rutrum, ligula enim ultricies sapien, sed eleifend ex velit sit amet libero. Sed 
ornare, ligula tempor tincidunt vulputate, justo tortor commodo ante, sit amet porta urna ante sed ex. Integer nec 
feugiat diam. Morbi felis libero, sagittis porta quam eu, tristique imperdiet nibh. In vulputate semper mi sed 
hendrerit. Sed at nibh varius, faucibus magna nec, fermentum magna. Suspendisse sed justo sit amet orci dignissim 
placerat eu sit amet turpis. Etiam eu elementum ante. Nullam maximus, purus pulvinar tincidunt tempor, libero leo 
consequat magna, sed hendrerit ante sem vel nisl. """

with open('lorem ipsum.txt', 'w+') as f:
    f.write(some_text)
    f.seek(0)  # we need to return to the top of the file before reading, otherwise we'll just read an empty string
    # line = read_line_by_line(f)
    # three_lines_taken = list(map(str.rstrip, itertools.islice(line, 3)))
    # for i in three_lines_taken:
    #     print(i)
    for i in read_line_by_line(f):
        print(i.rstrip())

rand_sequence = randoms(1, 10)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)

my_list = [1, 2, 3, 4, 5]
squares = [x**2 for x in my_list]
print(f'List comprehension: {squares}')
squares = (x**2 for x in my_list)
print(f'Generator: {squares}')
for i in squares:
    print(i)



