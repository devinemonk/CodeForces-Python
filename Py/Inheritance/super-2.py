class A:
    def m1(self):
        print("from A")
    pass

class B(A):
    def m1(self):
        print("from B")
    pass

class C(B):
    def m1(self):
        print("from C")
    pass


class D(C):
    def m1(self):
        print("from D")
        

class E(D):
    def m1(self):
        super(C , self).m1()
        print("from E")
        
e = E()
e.m1()


# Super method of C will executed --> B call
# from B
# from E
