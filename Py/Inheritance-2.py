

class P:
    a = 10
    
    def __init__(self):
        self.b = 20

        

class C(P):
    c = 30
    def __init__(self):
        self.d = 40
        super().__init__() #Need to invoke Parent constructor neccessary
    pass

a = C()
print(a.a)
print(a.b)
print(a.c)
print(a.d)
