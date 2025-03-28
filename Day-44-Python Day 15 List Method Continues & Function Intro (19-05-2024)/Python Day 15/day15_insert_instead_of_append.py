# insert instead of append
myList=["banana","mango","orange","kiwi"]
newList=[]
i=0
for item in myList:
    if "a" in item:
        newList.insert(i,item)
        i+1
print(newList)
