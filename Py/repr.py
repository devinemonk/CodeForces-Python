# Can convert object to string and string back to object


import datetime

x = datetime.datetime.now()
x1 = repr(x)
print(x1)
print(type(x1))
x2 = eval(x1)
print(x2)
print(type(x2))

# datetime.datetime(2023, 8, 2, 0, 43, 39, 614414)
# <class 'str'>
# 2023-08-02 00:43:39.614414
# <class 'datetime.datetime'>
