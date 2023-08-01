class Father:
    def show(self):
        print("Papa")
        
    def love(self):
        print("Papa loves more")
    

class Mother:
    def disp(self):
        print("Maa")
        
    def love(self):
        print("Maa loves more")
        
class Girl(Father , Mother):
    def __init__(self):
        self.show()
        self.disp()
        self.love()
        
        
        
class Boy(Mother , Father):
    def __init__(self):
        self.show()
        self.disp()
        self.love()
        
x = Girl()
print()
y = Boy()



# Papa
# Maa
# Papa loves more

# Papa
# Maa
# Maa loves more
