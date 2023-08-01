# Employee Has A Car

class Car:
    def __init__(self , model , name , color):
        self.model = model
        self.name = name
        self.color = color
        
    def show(self):
        print(self.model)
        print(self.name)
        print(self.color)

class Employee:
    
    def __init__(self , no ,name , car):
        self.no = no
        self.name = name
        self.car = car
        
    def show_details(self):
        print(self.no)
        print(self.name)
        self.car.show()
        

c = Car("XUV" , "XYZ" , "RED")
e = Employee(1, "Ram" , c)
e.show_details()


# ------
# OutPut

# 1
# Ram
# XUV
# XYZ
# RED
