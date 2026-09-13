# # Single Inheritance

# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name
        
# class Father(GrandFather):
#     def __init__(self, hobby, color, first_name):
#         super().__init__(color, first_name)
#         self.hobby = hobby
        
# gd1 = GrandFather('Red', 'Khan')
# f1 = Father('Cricket', 'red', 'khan')
# print(f1.color)

# Multiple and Multilevel Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    
    def gf_method(self):
        print("I am from GrandFather.")
        
class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby
    def father_method(self):
            print("I am from Father.")

class Children (Father, GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.fashion = fashion
    

c1 = Children("Test", "Badminton", "Red","Khan")
c1.gf_method()
c1.father_method()
print(c1.fashion, c1.color, c1.first_name)