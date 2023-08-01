# Employee IsA Person
# Employee HasA Car

class Car:
    def __init__(self , name , model , col):
        self.name = name 
        self.model = model
        self.col = col
        
    def disp_car(self):
        print(self.name + " "+ self.model + " "+ self.col)


class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def disp(self):
        print("Yipee")
        
        
class Employee(Person):
    def __init__(self , name , age , id , sal , car):
        super().__init__(name , age)
        self.id = id 
        self.sal = sal
        self.car = car
        
    def code(self):
        print("coding in python")
        
    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.sal)
        self.car.disp_car()
        
c = Car("X" , "Y" , "Z")
e = Employee("Ram" , "22" , 1 ,100000 , c)
e.disp()
e.code()
e.display()




# Yipee
# coding in python
# Ram
# 22
# 1
# 100000
# X Y Z
