class A:
    a = 1
    def __init__(self):
        b = 2
    
    def do(self):
        print("do")
        
    @classmethod
    def bo(cls):
        print("bo")
        
    @staticmethod
    def ao():
        print("ao")
    pass

class B(A):
    a = 3
    def __init__(self):
        self.b = 4
        print(self.a)
        print(self.b)
        print(super().a)
        super().do()
        super().bo()
        super().ao()
        # print(super().b)
    pass

b = B()


# 3
# 4
# 1
# do
# bo
# ao
