class Book:
    def __init__(self , pages):
        self.pages = pages
        
    def __add__(self , other): #magic_methods
        return self.pages + other.pages
        
A = Book(10)
B = Book(20)
print(A+B)

# 30
