# List comprehension
myList = ["kiwi","orange"]
newList = [x if "a" in x else "not present" for x in myList]
newList = [x for x in myList if "a" in x]
print(newList)
newList = [x.upper() for x in myList if "a" in x]
print(newList)