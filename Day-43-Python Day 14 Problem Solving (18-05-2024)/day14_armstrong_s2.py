# armstrong series
armstrong_series =[]
for i in range(1000):
    check_num = i
    sum=0
    for j in str(check_num):
        sum+=int(j)**len(str(check_num))
    if sum == check_num:
        armstrong_series.append(check_num)
print(armstrong_series)