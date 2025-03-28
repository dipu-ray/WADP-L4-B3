# Leap year
user_input=[2020, 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]
for x in user_input:
    if x%100==0:
        if x%400==0:
            print(f"{x} is leap year")
        else:
            print(f"{x} is not leap year")
    elif x%4==0:
        print(f"{x} is leap year")
    else:
        print(f"{x} is not leap year")