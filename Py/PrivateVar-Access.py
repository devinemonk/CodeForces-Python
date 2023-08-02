class Test:
    __x = 1
    
    def __init__(self):
        self.__y = 2
        
        
t = Test()
print(t.__dict__)
print(t._Test__y)
print()
print(Test.__dict__)
print(Test._Test__x)


# {'_Test__y': 2}
# 2

# {'__module__': '__main__', '_Test__x': 1, '__init__': <function Test.__init__ at 0x7fcca18a6c00>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
# 1
