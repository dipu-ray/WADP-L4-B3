# List sorting
myList = [2,5,3,1,6,9,6,5]
# ascending
myList.sort()
print(myList)
# decending
myList.sort(reverse=True)
print(myList)

myList2=["banana","15","Kiwi","cherry"]
myList2.sort(key=str.lower)
print(myList2)
