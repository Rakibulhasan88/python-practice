def addition(*args):
    print(args)
    return sum(args)

r = addition(12, 10, 5, 3, 2, 1)
print(r)