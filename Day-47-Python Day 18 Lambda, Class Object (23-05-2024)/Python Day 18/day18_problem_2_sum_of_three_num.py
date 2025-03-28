# Lambda problem 2 : Sum of 3 number using Lambda
def myfunc(x,y,z):
  return lambda a,b,c : a+b+c+x+y+z

mydoubler = myfunc(1,1,1)
mytripler = myfunc(2,2,2)

print(mydoubler(1,2,3)) 
print(mytripler(4,5,6))
