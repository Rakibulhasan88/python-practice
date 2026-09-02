# print("Hello World!!\nThis is my First code!!") 
# b="Rakib"
# print(len(b))

# rain=int(input())
# if rain==1:
#     print("Take Umbrella")
# else:
#     print("No need to take Umbrella")

# def my_first_function():
#     print("Hello from a function")
    
# my_first_function() 

# def add_two_numbers(a, b):
#     return a + b

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# result = add_two_numbers(a, b)
# print("The sum is:", result)

# number = [1,2,3,4,5]
# sqr_nums = list(map(lambda x: x*x, number))
# print(sqr_nums)

# # filter
# even_nums = list(filter(lambda x: x%2==0, number))
# print(list(even_nums))

# #reduce
from functools import reduce
def outer():
    n= "enclosing"
    def inner():
        n= "local"
        print(n)
    inner()
    print(n)
outer()
