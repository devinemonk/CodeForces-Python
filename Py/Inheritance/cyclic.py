class A(A):
    def __init__(self):
        print("trying")
    pass


a = A()


# ERROR!
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'A' is not defined


# Python (No Language) supports cyclic inheritance
