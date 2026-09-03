# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in a:
#     print(item)

# for i in range(10):
#     print(f"Loading... {i}%")
# print("Loading Complete!")

# a = [1, 2, 3, 4, "a", 5, 6, 7, 8, 9, 10]

# for i in a:
#     if type(i) == str:
#         break
#     else:
#         print(i)

# a = [1, 2, 3, 4, "a", 5, 6, 7, 8, 9, 10]

# for i in a:
#     if type(i) == str:
#         continue
#     else:
#         print(i)

#List Comprehension

a=[1,10,23,24,90,100,200,300,400,500]

result = []

# Normal way
for i in a:
    if i%2 == 0:
        result.append(i)
print(result)

#List Comprehension
new_result = [i for i in a if i%2 == 0]
print(new_result)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_new_result = []
for i in b:
    if i%2 == 0:
        b_new_result.append(i**2)
    else:
        b_new_result.append(i)
print(b_new_result)

b_new = [i**2 if i%2 == 0 else i for i in b]
print(b_new)