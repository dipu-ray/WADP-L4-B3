# fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
user_input=100
f_series=[]
a=0
b=1
for _ in range(user_input):
    f_series.append(a)
    next_number=a+b
    a=b
    b=next_number
print(f_series)
    