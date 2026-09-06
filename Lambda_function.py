import functools

#anonymous functions --> Unnamed functions
# print not used in the program
# only returns the value of the function

# def square(x):
#     return x * x
# print(square(5))

# square = lambda x: x * x
# print(square(4))

# add = lambda a, b : a + b
# print(add(5, 6))

# Sorting a list of tuples based on the second element of each tuple

students = [('Rakib', 60), ('Hasan', 80), ('Fahim', 70), ('Rafi', 90)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)

#map(), filter(), reduce() functions

# Map
nums = [1, 2, 3, 4, 5]
sq_nums = list(map(lambda x: x*x, nums))
print(sq_nums)

#filter
even =list(filter( lambda x: x % 2 == 0, nums))
print(even)

# reduce
sum = functools.reduce(lambda x, y: x + y, nums)
print(sum)