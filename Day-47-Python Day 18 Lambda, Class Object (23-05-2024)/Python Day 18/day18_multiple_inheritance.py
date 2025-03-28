# Multiple Inheritance
class c():
    y=20
class a():
    x=10
class b(a,c):
    pass
obj1 = b()
print(obj1.x)
print(obj1.y)