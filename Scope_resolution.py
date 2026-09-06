# scope --> a region where a variable is accessible. In python, there are 4 types of scope:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. Built-in scope

x = 10 # global variable

# def function():
#     y = 219 # local variable
#     print("y:", y)
#     print(x) # 20

# function()

# n = "global" # global variable

def outer():
    n = "Enclosing" # Enclosing variable
    def inner():
        global n # global variable
        n = "Local" # Local variable
        print(n)
    inner()
outer()
print(n) # Local

        