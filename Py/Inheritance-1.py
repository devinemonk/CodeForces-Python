# Is A Relationship

class P:
    a = 10
    
    def __init__(self):
        self.b = 20
        
    @classmethod
    def show(cls):
        print("class method of P")
        
    @staticmethod
    def display():
        print("static method of P")
        
    def disp(self):
        print("method of P")
        

class C(P):
    pass

a = C()
print(a.a)
print(a.b)
a.show()
a.display()
a.disp()

# -----------
#Output

# 10
# 20
# class method of P
# static method of P
# method of P
