# def info():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     return f"Name: {name}, Age: {age}"

# print(info())

# mx = max([1, 2, 3, 4, 5])
# print(f"Maximun value is: {mx}. {mx*3}")

def Calculator():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    operation = input("Enter operation (+, -, *, /):")
    
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
result = Calculator()
print(f"Result: {result}")
    