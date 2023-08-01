class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def disp(self):
        print("Yipee")
        
        
class Employee(Person):
    def __init__(self , name , age , id , sal):
        super().__init__(name , age)
        self.id = id 
        self.sal = sal
        
    def code(self):
        print("coding in python")
        
    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.sal)
        
e = Employee("Ram" , "22" , 1 ,100000)
e.disp()
e.code()
e.display()


# Output

# Yipee
# coding in python
# Ram
# 22
# 1
# 100000
