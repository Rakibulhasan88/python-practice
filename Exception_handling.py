# errors vs Exceptions
# Compile Time, Run Time
# Errors --> Compile Time (Syntex, Indentation)
# Exceptions  --> Run Time Error (Indexing, key, value, zero division)

try:
    with open("file.txt", 'r') as f:
        print(f.read())
    print(10/0)
    x = int("abc")
    a = [1, 2, 3]
    print(a[100])
    x = abc
except ZeroDivisionError:
    print("Error : Division by zero is not possible.")
except FileNotFoundError:
    print("File Not Found")
except ValueError:
    print("Invalid Value")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print("Sone error occurred!!", e)