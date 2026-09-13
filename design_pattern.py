# Singleton

class Singleton:
    _instance = None #class variable
    
    def __new__(cls):
        if cls._instance is None:
            print("1st obj is created")
            cls._instance = super(Singleton, cls).__new__(cls)
            
ob1 = Singleton()
ob2 = Singleton()

print(ob1 is ob2)