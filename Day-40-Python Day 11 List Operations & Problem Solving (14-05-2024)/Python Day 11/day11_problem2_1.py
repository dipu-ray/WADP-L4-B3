'''
- Problem 02
   - Input n numbers item(positive integer) in a list
   - Separate Even numbers from the list and store it in Even_List then sum the Even list number
   - Separate Odd numbers from the list and store it in Odd_List then sum the Odd list number
   - Summation the main_list
   - Check main_list summation == Even_list + Odd_list summation
   - If Equal print Hello.
'''
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
    else:
        print(f"Only input positive integer, {user_in} is not positive integer")

print(f"Main List: {main_list}")

for x in main_list:
    if x%2==0:
        Even_List.append(x)
    else:
        Odd_List.append(x)
print(f"Stored Even List: {Even_List}")
print(f"Stored Odd List: {Odd_List}")

for x in Even_List:
    Even_List_Sum+=x
print(f"Sum of Even List: {Even_List_Sum}")

for x in Odd_List:
    Odd_List_Sum+=x
print(f"Sum of Odd List: {Odd_List_Sum}")

Even_Odd_Sum = Even_List_Sum+Odd_List_Sum
print(f"Sum of Even & Odd: {Even_Odd_Sum}")

for x in main_list:
    Main_List_Sum+=x
print(f"Sum of Main List: {Main_List_Sum}")

if Main_List_Sum == Even_Odd_Sum:
    print("Hello")
