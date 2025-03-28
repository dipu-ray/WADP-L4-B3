bkash_menu = '''
1. Send Money
2. Send Money to Non-Bkash User
3. Mobile Recharge
4. Payment
5. Cash Out
6. Pay Bill
7. Microfinance
8. Download Bkash App
9. My Bkash
10. Reset Pin
'''
print(bkash_menu)

choice = int(input("Enter your choice: "))

print(f'You choose: {choice}')

if choice==1:
    receiver_number = int(input("Enter receiver number: "))
    if receiver_number:
        amount = int(input("Enter amount: "))
        if amount:
            pin = int(input("Enter pin: "))
            if pin:
                print(f"{amount} BDT Sent Successful to {receiver_number}")
            else:
                print("Please enter valid number")
        else:
            print("Please enter valid pin")
    else:
        print("please enter valid number")