'''
myList=[0,1,2,6,3,4,3,3,6]
In the given list if 5 number item is equal to the length of list print hello
'''

myList=[0,1,2,6,3,4,3,3,6]

fifth_item=myList[5-1]
print(f"Fifth item is: {fifth_item}")

list_length=len(myList)
print(f"List length is: {list_length}")

if fifth_item==list_length:
    print("hello")
else:
    print(f"Fifth item: {fifth_item} is not equal to list length {list_length}")