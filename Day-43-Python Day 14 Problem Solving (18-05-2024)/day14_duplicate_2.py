myList=[1,2,3,5,3,4,4,6,2,1,1]
uniqueList=[]
duplicateList=[]

for item in myList:
    if item not in uniqueList:
        uniqueList.append(item)
    else:
        duplicateList.append(item)

print(f"Original List: {myList}")
print(f"Unique List: {uniqueList}")
print(f"Duplicate List: {duplicateList}")
