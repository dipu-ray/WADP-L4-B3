'''
myList=[0,1,2,6,3,4,3,3,6]
In list if 5 number item occur 3 times print hello
'''
myList=[0,1,2,6,3,4,3,3,6]
count=0

fifth_item = myList[5-1]

for x in myList:
    if fifth_item==x:
        count+=1
        if count >= 3:
            print("Hello")