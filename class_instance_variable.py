class School:
    school_name = "Daffodil International University" #Class variable
    
    def __init__(self, name):
        self.student_name = name #Instance variable
    
sc1 = School("Rahim")
sc2 = School("Karim")
School.school_name ="ABCD School"
print(sc1.school_name)
print(sc2.student_name)
print(sc2.school_name, sc2.student_name)