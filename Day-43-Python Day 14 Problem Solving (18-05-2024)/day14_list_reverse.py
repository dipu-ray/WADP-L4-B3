# list item reverse
myList=[1,2,3,4,5,6,7,8,9]
reverseList=[]
for x in range(len(myList)):
    index=x+1
    reverseList.append(myList[-index])
print(reverseList)