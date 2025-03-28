# main_list=[1,2,3,4,5]
# print(f"Main List: {main_list}")

main_list=[]
Even_List=[]
Odd_List=[]
Main_List_Sum=0
Even_List_Sum=0
Odd_List_Sum=0

user_input_count = int(input("How many positive integer number you want to input: "))
for x in range(user_input_count):
    user_in = int(input("Enter list item: "))
    if user_in>=0:
        main_list.append(user_in)
        if user_in%2==0:
            Even_List.append(user_in)
            Even_List_Sum+=user_in
        else:
            Odd_List.append(user_in)
            Odd_List_Sum+=user_in
        Even_Odd_Sum = Even_List_Sum+Odd_List_Sum
        Main_List_Sum+=user_in
    else:
        print(f"Only input positive integer, {user_in} is not positive integer")
print(f"Main List: {main_list}")
print(f"Stored Even List: {Even_List}")
print(f"Stored Odd List: {Odd_List}")
print(f"Sum of Even List: {Even_List_Sum}")
print(f"Sum of Odd List: {Odd_List_Sum}")
print(f"Sum of Even & Odd: {Even_Odd_Sum}")
print(f"Sum of Main List: {Main_List_Sum}")
if Main_List_Sum == Even_Odd_Sum:
    print("Hello")
else:
    print("Not Equal")
