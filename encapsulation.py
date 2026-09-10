# # Public Members
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
# emp = Employee('Rakib', 5000)
# print(emp.name)
# print(emp.salary)

# Protected Members
class Company:
    def __init__(self):
        self._project = "AI System" #Protected Attribute
        
class TechCompany(Company):
    def show_project(self):
        print(f'working on: {self._project}')
        
comp = TechCompany()
comp.show_project()
print(comp._project)