# For file open
# file = open('file.txt', 'r')
# content = file.read()
# print(content)

# file.close() #for file close

# Professional way to open a file using 'with' statement
# with open('file.txt', 'r') as f:
#     content = f.read()
#     print(content)
    
# Professional way to write to a file using 'with' statement
# with open('file.txt', 'w') as f:
#     f.write("This is Rakibul Hasan.")
#     f.write("\nI am a Python Developer.")
#     f.write("\nStuded at Daffodil International University.")

# More function to file handling

import os
import pathlib 
if os.path.exists('file.txt'):
    print("File exists")
else:
    print("File does not exist")
    
file_path = pathlib.Path('file.txt')

if file_path.exists():
    print("File exists")
print(os.path.abspath('file.txt'))
print(os.path.getsize('file.txt'))

with open('file.txt', 'r') as f:
    print(f.read(5))