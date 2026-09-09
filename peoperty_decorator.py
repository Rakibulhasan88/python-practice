# property decorator function we only can see, we can't update this

class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
    
ob1 = Employee("Rakib", 40000)
# print(ob1._salary)
# print(ob1.get_salary)
ob1.salary = 70000
print(ob1._salary)