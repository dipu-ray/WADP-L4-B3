total_user_input = int(input("How many number you want to input: "))
userList = []
for x in range(total_user_input):
    user_input = int(input(f"Enter item number {x+1} of {total_user_input}:"))
    user_input = int(input("Enter item number {} of {}:".format(x+1,total_user_input)))
    userList.append(user_input)
print(userList)