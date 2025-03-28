# Multi level Inheritance
class c:
    y=20
class a(c):
    x=10
class b(a):
    pass
obj1 = b()
print(obj1.x)
print(obj1.y)