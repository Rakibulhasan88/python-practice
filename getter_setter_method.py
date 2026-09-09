class Employee:
    company_name = "Ostad Linited"
    
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #Protected Variable, by convention, _variable name eta dhora hoy private variable, but logivally private hoy na
        
    def get_salary(self, password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Access!!!")
            
    def set_salary(self, password, salary):
            if password == "admin":
                self._salary = salary
                print(f"New Salary : {self._salary}")
            else:
                print("Invalid Access!!!")

ob1 = Employee("Rakib", 30000)
ob2 = Employee("Karim", 50000)

ob1._salary = 60000
print(ob1._salary)