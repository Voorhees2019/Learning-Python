# from collections import Counter
#
#
# zen = """Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""
#
#
# cleaned_list = []
#
# for word in zen.split():
#     cleaned_list.append(word.strip('.,*!-').lower())
#
# print(Counter(cleaned_list).most_common(5))
# print(cleaned_list)


# set1 = set()
# set2 = set()
# for i in range(10):
#     if i % 2:
#         set1.add(i)
#     else:
#         set2.add(i)
#
# print(set1)
# print(set2)


# import random
#
#
# numbers = []
#
# numbers_size = random.randint(10, 15)
# for _ in range(numbers_size):
#
#     numbers.append(random.randint(10, 20))
# print(numbers)
#
# numbers.sort()
# half_size = len(numbers) // 2
# median = None
#
# if numbers_size % 2 == 1:
#     median = numbers[half_size]
# else:
#     median = sum(numbers[half_size - 1:half_size + 1]) / 2
#
# print(median)
#
#
# import statistics
#
#
# statistics.median(numbers)


# def get_multiplier():
#     def inner(a, b):
#         return a * b
#     return inner
#
#
# multiplier = get_multiplier()
# print(multiplier(5, 6))


# def get_multiplier(number):
#     def inner(a):
#         return a * number
#     return inner
#
#
# multiplier_by_2 = get_multiplier(2)
# print(multiplier_by_2(50))


# list1 = [i for i in range(11)]
#
#
# def func(*list_):
#     list2 = [str(i) for i in list_]
#     return list2
#
#
# var1 = func(*list1)
# print(var1)
# print(type(var1[1]))


# def stringify_list(num_list):
#     return list(map(str, num_list))
#
#
# print(stringify_list(range(11)))


# from functools import partial
#
#
# def greeter(person, greeting):
#     return "{}, {}!".format(greeting, person)
#
#
# hier = partial(greeter, greeting = 'Hi')
# helloer = partial(greeter, greeting = 'Hello')
#
# print(hier('brother'))
# print(helloer('sir'))

# print(list(zip(filter(bool, range(3)), [x for x in range(3) if x])))


# def stringify(func):
#   return str(func)
#
#
# @stringify
# def multiply(a, b):
#   return a * b
#
#
# multiply(10, 2)  # TypeError: 'str' object is not callable


# import functools
#
#
# def logger(func):
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         result = func(*args, **kwargs)
#         with open('log.txt', 'w') as f:
#             f.write(str(result))
#         return result
#
#     return wrapped
#
#
# @logger
# def summator(num_list):
#     return sum(num_list)
#
#
# print('Summator: {}'.format(summator([i for i in range(6)])))
# with open('log.txt', 'r') as f:
#     print('log txt: {}'.format(f.read()))
#
# print(summator.__name__)


# def logger(filename):
#     def decorator(func):
#         def wrapped(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(filename, 'w') as f:
#                 f.write(str(result))
#             return result
#         return wrapped
#     return decorator
#
#
# @logger('new_log.txt')
# def summator(num_list):
#     return sum(num_list)
#
#
# # summator = logger('log.txt')(summator)
# # print(summator([1, 2, 3, 4, 5]))
#
# with open('new_log.txt', 'r') as f:
#     print(f.read())


# def first_decorator(func):
#     def wrapped():
#         print('Inside first decorator product.')
#         return func()
#     return wrapped
#
#
# def second_decorator(func):
#     def wrapped():
#         print('Inside second decorator product.')
#         return func()
#     return wrapped
#
#
# @first_decorator
# @second_decorator
# def decorated():
#     print('Finally called...')
#
#
# # decorated = first_decorator(second_decorator(decorated))
# decorated()


# def even_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 2
#
#
# for number in even_range(0, 11):
#     print(number, end =" ")


# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print('After yielding: {}'.format(item))
#
#
# # generator = list_generator([1, 2])
# # print(next(generator))
# for i in list_generator([1, 2]):
#     print(i)


# def fibonacci(number):
#     a = b = 1
#     for _ in range(number):
#         yield a
#         a, b = b, a + b
#
#
# for num in fibonacci(10):
#     print(num)


# def accumulator():
#     total = 0
#     while True:
#         value = yield total
#         print('Got: {}'.format(value))
#
#         if not value: break
#         total += value
#
#
# generator = accumulator()
# print(next(generator))
# print('Accumulated: {}'.format(generator.send(2)))
# print('Accumulated: {}'.format(generator.send(10)))


# def nearest(list, target):
#     return min(list, key=lambda x: abs(x-target))
#
#
# l = [1, 69, 43, 68, 65, 25, 87, 67]
# print(nearest(l, 66))


# print("Enter 'x' for exit.")
# hexdec = input("Enter any number in Hexadecimal Format: ")
# if hexdec == 'x':
#     exit()
# else:
#     dec = int(hexdec, 16)
#     print(hexdec, "in Binary =", bin(dec))


