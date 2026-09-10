# Public Members
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
emp = Employee('Rakib', 5000)
print(emp.name)
print(emp.salary)