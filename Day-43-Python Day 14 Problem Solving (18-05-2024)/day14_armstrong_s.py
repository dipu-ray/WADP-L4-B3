# logic building code for creating the series of armstrong number
armstrong_series1=[407]
for i in armstrong_series1:
    check_num = i
    sum=0
    for j in str(check_num):
        sum+=int(j)**len(str(check_num))
    if sum == check_num:
        print(check_num)