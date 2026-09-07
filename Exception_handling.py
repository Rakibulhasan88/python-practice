# errors vs Exceptions
# Compile Time, Run Time
# Errors --> Compile Time (Syntex, Indentation)
# Exceptions  --> Run Time Error (Indexing, key, value, zero division)


try:
    with open("file.txt", 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")