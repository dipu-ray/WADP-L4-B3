# Minimum number from list
myList=[1,11,3,100,2,222,4,2]
min=0
for item in myList:
    temp=item
    for j in myList:
        if j<temp:
            min=j
print(min)