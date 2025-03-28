# Armstrong number
num = 8208
sum=0
for x in str(num):
    sum += int(x)**len(str(num))
print(sum)

