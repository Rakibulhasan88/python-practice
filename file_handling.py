# file=open('file.txt','r')
# content=file.read()
# print(content)

# file.close()

# with open('file.txt','r') as f:
#     content=f.read()
#     print(content)
    
# with open('file.txt','w') as f:
#     f.write('\n Hello World\n')
#     f.write("i am Rakibul Hasan\n")

import os
import pathlib
if os.path.exists('file.txt'):
    print("This file exists")
else:
    print("This file does not exist")

file_path= pathlib.Path('file.txt')

if file_path.exists():
    print("this file exists")
print(os.path.abspath('file.txt'))
print(os.path.getsize('file.txt'))