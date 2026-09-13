# poly -> multiple
# morphism --> form

# # 1. Method Overriding
# class GrandFather:
#     def greet(self):
#         print("Grandfather says")
        
# class Father:
#     def greet(self):
#         print("father says")
        
# class Children:
#     def greet(self):
#         print("Childeren says")
        
# gf = GrandFather()
# f = Father()
# c = Children()

# gf.greet()
# f.greet()
# c.greet()


# 2. Method Overloading
class Shape:
    def area():
        return 10
    
    def area(self, a, b=10):
        return a*b
    
p =Shape()
print(p.area(12))
print(p.area(12,10))