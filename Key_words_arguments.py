# def my_func(f_name, l_name, age):
#     print(f"First name: {f_name}, Last name: {l_name}, Age: {age} years old.")

# # my_func("John", "Doe", 30)
# my_func(age = 30, l_name = "Doe", f_name = "John")

# Arbitary Number of key word arguments

def my_func(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}, I am {kwargs['age']} years old. I got {kwargs['marks']} marks in my last exam.")
    
my_func(age = 30, l_name = "Doe", f_name = "John", marks =90)