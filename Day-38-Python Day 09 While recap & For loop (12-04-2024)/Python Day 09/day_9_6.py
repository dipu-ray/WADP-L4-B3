# i=10
user_input=int(input("Input N: "))
i=user_input-1
print('Natural numbers from 10-1 in reverse: ')
while i<=user_input:
    if i==0:
        break
    print(f'{i}',end=", ")
    i-=1

