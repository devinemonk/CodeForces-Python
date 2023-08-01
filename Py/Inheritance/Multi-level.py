class G:
    def show(self):
        print("Gramps")

class P(G):
    def show(self):
        super().show()
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


# Gramps
# Parent
# child
# HEYYY
