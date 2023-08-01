class P:
    def show(self):
        print("Parent")
        
    def disp(self):
        print("HEYYY")
        
class C(P):
    def show(self):
        super().show()
        print("child")
        
x = C()
x.show()
x.disp()



# Parent
# child
# HEYYY
