class G:
    def show(self):
        print("YO YO")

class P(G):
    def show(self):
        super().show()
        print("WONG")
        
    
        
class C(G):
    def show(self):
        super().show()
        print("DEEE")
        
x = C()
x.show()
print()
y= P()
y.show()



# YO YO
# DEEE

# YO YO
# WONG
