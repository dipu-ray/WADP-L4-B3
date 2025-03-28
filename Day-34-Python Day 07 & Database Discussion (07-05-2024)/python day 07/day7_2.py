a=1
b=2
c=3
d=4
e=5

if a>b:
    if a>c:
        print("a greater")
    else:
        print("c greater")

else:
    if b>c:
        print("b greater")
    else:
        print("c greater")

# a,b,c
print("a greater")if (a>b and a>c) else print("b is greater") if b>c else print("c is greater")

# a,b,c,d
print("a is greater") if (a>b and a>c and a>d) else print("b is greater") if b>c and b>d else print("c is greater") if c>d else print("d is greater")

# a,b,c,d,e
print("a is greater") if (a>b and a>c and a>d and a>e) else print("b is greater") if b>c and b>d and b>e else print("c is greater") if c>d and c>e else print("d is greater") if d>e else print("e is greater")
