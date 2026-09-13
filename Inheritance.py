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

# # Multiple and Multilevel Inheritance

# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name
    
#     def gf_method(self):
#         print("I am from GrandFather.")
        
# class Father(GrandFather):
#     def __init__(self, hobby, color, first_name):
#         super().__init__(color, first_name)
#         self.hobby = hobby
#     def father_method(self):
#             print("I am from Father.")

# class Children (Father, GrandFather):
#     def __init__(self, fashion, hobby, color, first_name):
#         super().__init__(hobby, color, first_name)
#         self.fashion = fashion
    

# c1 = Children("Test", "Badminton", "Red","Khan")
# c1.gf_method()
# c1.father_method()
# print(c1.fashion, c1.color, c1.first_name)

# # 4. Hierarchical Inheritance
# class Vehicle:
#     def engine_type(self):
#         print("Vehicle has an engine")
        
# class Car(Vehicle):
#     def num_doors(self):
#         print("Car has 4 doors")
        
# class Truck(Vehicle):
#     def load_capacity(self):
#         print("Truck can carry 10 tons")
        
# car = Car()
# car.engine_type()
# car.num_doors()
# Truck = Truck()
# Truck.engine_type()
# Truck.load_capacity()

# 5. Hybrid

class Shape:
    def area(self):
        print("Calculating area ...")
        
class Polygon(Shape):
    def sides(self):
        print("Poplygon has multiple sides.")
        
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length*self.breadth
    
rec = Rectangle(10, 5)
rec.sides()
print(rec.area())
rec.area()