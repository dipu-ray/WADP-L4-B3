# problem: what is the index of 8 when it occur 2nd time
thistuple = (1, 3, 4, 8, 4, 3, 2, 4, 8, 4, 3)
count = 0
i=0
for x in thistuple:
    if x == 8:
        i += 1
    if x==8 and i == 2:
        print(count)
    count+=1

# without using i=0:
# problem: what is the index of 8 when it occur 2nd time (another approach)
thistuple = (1,3,4,8,4,3,2,4,8,4,3,8,2,5,6,8,5,3,4,8)
count = 0
for i in range(len(thistuple)):
    if thistuple[i] == 8:
        count+=1
    if thistuple[i]==8 and count == 5:
        print(i)

