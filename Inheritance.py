# Single Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
        
class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby
        
gd1 = GrandFather('Red', 'Khan')
f1 = Father('Cricket', 'red', 'khan')
print(f1.color)
        