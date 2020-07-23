# def f(arr):
#     arr[1] = 0
#

arr = [38, 27, 43, 3, 9, 82, 10]
# f(arr)
print(arr)
mid = len(arr) // 2
print(mid)
L = arr[:mid]  # Dividing the array elements
print(L)
R = arr[mid:]
print(R)
# y = 501 + 499
# print(y.__doc__)
# y.__doc__
# print(x is y)
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# print("################################################")
#
# a, *rest = [1, 2, 3]
# print(a)
# print(rest)
# print("################################################")
#
# filename = 'foobar.txt.efefe.grgr.htht'
# basename, __, ext = filename.rpartition('.')
# filename.split('.', 1)
# print(basename)
# print(ext)
# print("################################################")
#
# four_lists = [[] for __ in range(4)]
# print("################################################")

# letters = ['s', 'p', 'a', 'm']
# word = ''.join(letters)
# print(word)
# print("################################################")
#
# s = set(['s', 'p', 'a', 'm', 'm'])
# l = ['s', 'p', 'a', 'm']
# print(s)
# print(l)

# d = {'hello': 'world'}
#
# if 'hello' in d:
#     print(d['hello'])
#
# print(d.get('hello'))

# x = [i ** 2 for i in range(10)]
# y = list(map(lambda x: x ** 2, range(10)))
# print(x)
# print(y)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# x = [[row[i] for row in matrix] for i in range(4)]
# print(x)
#
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# sequence = [3, 4, 5]
# print(sequence)
# filtered_values1 = [value for value in sequence if value != 4]
# print(filtered_values1)
# filtered_values2 = (value for value in sequence if value != 4)
# print(filtered_values2)

# sequence[::] = [value for value in sequence if value != 4]
# print(sequence)
#
# a = [3, 4, 5]
# b = a  # a and b refer to the same list object
# print(a)
# print(b)
# for i in range(len(a)):
#     a[i] += 3
# a = [i + 3 for i in a]
# print(a)
# print(b)

# with open("") as f:
#     for line in f:
#         splited_line = line.split(',', 1)
#         if len(splited_line) > 1:
#             print(splited_line[1])
#
# lambda x: x ** 2, range(10)

# create a concatenated string from 0 to 19 (e.g. "012..1819")

#
# print(''.join([str(i) for i in range(20)]))
#
# foo = 'foo'
# bar = 'bar'
# print('{fo}{ba}'.format(fo=foo, ba=bar))
