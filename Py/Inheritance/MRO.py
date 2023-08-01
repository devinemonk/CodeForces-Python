class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


print(D.mro())
    
#Tell the order of inheritance function check
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# In python every class inherits object classs
