# Class object creation
class MyClass:
    x=5

p1 = MyClass()
print(p1.x)
MyClass.x=80
print(p1.x)
p1.x=8
print(p1.x)

id = MyClass()
age = MyClass()
length = MyClass()

id.x=1
print(id.x)
age.x=22
print(age.x)
length.x=100
print(length.x)