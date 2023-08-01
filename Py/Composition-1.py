#Car has - a Engine 

class Engine:
    a = 10
    def __init__(self):
        self.b = 20
        
    def update(cls ,x):
        cls.a = x
    
    @staticmethod    
    def show():
        print("Engine Class")
        

class Car:
    def __init__(self):
        self.e = Engine()
        
    def show(self):
        print("Inside the Car callling Engine")
        print(self.e.a)
        print(self.e.b)
        self.e.show()
        
        
c =Car()
c.e.update(7)
c.show()

# Output
# Inside the Car callling Engine
# 7
# 9
# 20
# Engine Class
