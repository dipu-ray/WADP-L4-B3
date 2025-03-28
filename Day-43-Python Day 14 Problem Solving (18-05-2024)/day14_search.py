# Searching from list
myList=[1,2,3,5,3,4,4,6,2,1,1]
search = 2
count=0
for item in myList:
    if search == item:
        count+=1
print(f"Item {search} found {count} times")