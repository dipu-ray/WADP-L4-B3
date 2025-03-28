'''
myList=[0,1,2,6,3,4,3,3,6]
In the given list remove duplicate
'''
myList=[0,1,2,6,3,4,3,3,6]
index = 0
while index<len(myList):
    item = myList[index]
    for duplicate_index in range(index + 1, len(myList)):
        if myList[duplicate_index] == item:
            myList.pop(duplicate_index)
            break
    else:
        index += 1
print("List with duplicates removed:", myList)
