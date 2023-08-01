class A:
    def talk(self):
        print("Hey")
        
class B:
    def bark(self):
        print("Bark")
        
def voice(obj):
    if hasattr(obj , 'talk'):
        obj.talk()
        
    elif hasattr(obj , 'bark'):
        obj.bark()
        

voice(A())
voice(B())


# Hey
# Bark
