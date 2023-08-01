class Test:
    
    def dope(self , *b ):
        x = 0
        for i in b:
            x+=i
        print(x)
    
        
a = Test()
a.dope()
a.dope(1,3)
a.dope(8,5,3,0,6)


# 0
# 4
# 22
