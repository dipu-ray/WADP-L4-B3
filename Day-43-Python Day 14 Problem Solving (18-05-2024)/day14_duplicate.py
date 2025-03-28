myList=[1,1,1,2,2,3,3,4,4,5,6]
# myList=[1,2,3,5,4,6]
count = 0
for item in myList:
    temp = item
    for j in myList:
        if j == temp:
            count+=1
            if count>1:
                myList.remove(j)
    count=0
print(myList)