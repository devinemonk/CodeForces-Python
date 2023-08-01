class A(A):
    def __init__(self):
        print("trying")
    pass



# ERROR!
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'A' is not defined


# Python (No Language) supports cyclic inheritance
# ----------------------------


class C(B):
    pass

class B(C):
    pass

# ERROR!
# Traceback (most recent call last):
#   File "<string>", line 7, in <module>
# NameError: name 'B' is not defined
