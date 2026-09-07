# For file open
file = open('file.txt', 'r')
content = file.read()
print(content)

file.close() #for file close

# Professional way to open a file using 'with' statement
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
    
# Professional way to write to a file using 'with' statement
with open('file.txt', 'w') as f:
    f.write("This is a sample text written to the file.")
    