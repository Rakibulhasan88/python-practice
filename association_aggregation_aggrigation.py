# # Association

# class Laptop:
#     def __init__(self, brand):
#         self.brand = brand
        
        
# class Student:
#     def __init__(self, name, laptop_obj):
#         self.name = name
#         self.laptop_v = laptop_obj
    
#     def show_laptop_info(self):
#         print(f"{self.name} has a laptop named {self.laptop_v.brand}")
        
# lp1 = Laptop("Asus")
# student = Student("Rakib",lp1)
# print(student.show_laptop_info())


# Aggregation : has a relationship
# A university has departments

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        
    def add_department(self, department):
        self.departments.append(department)
    
    def show_departments(self):
        return [department.name for department in self.departments]

uni1 = University("Daffodil")
uni2 = University("City")
dept1 = Department("Programming")
dept2 = Department("Math")
dept3 = Department("Data Science")
uni1.add_department(dept1)
uni1.add_department(dept2)
uni2.add_department(dept1)
uni2.add_department(dept2)
uni2.add_department(dept3)
print(uni2.show_departments())
print(uni1.show_departments())