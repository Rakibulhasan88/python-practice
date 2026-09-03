a = {'Rahim' : 12, 'Karim' : 14, 'Jabbar' : 15, 'Sakib' : 16, 1 : [1,2,3,4], 2 : {3,4,5}}

print(type(a))

for i in a:
    print(i)
    
for i in a.values():
    print(i)

print(a.keys(), a.values())

#key value pair together

for k,v in a.items():
    print(f"Key Name : {k}, Values {v}")
   
# List to Dictionary 
a = [1,2,3]
b = ["Mango", "Banana", "Orange"]

print(dict(zip(a,b)))