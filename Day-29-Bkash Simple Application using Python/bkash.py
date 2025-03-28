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
elif choice==2:
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
            print("Please enter valid amount")
    else:
        print("please enter valid number")
elif choice==3:
    operator = int(input('''
Choose Operator:
1. Robi
2. Airtel
3. Banglalink
4. Grameenphone
5. Teletalk
    '''))
    if operator:
        mobile_number = int(input("Enter mobile number: "))
        if mobile_number:
            recharge_amount=int(input("Enter recharge amount: "))
            if recharge_amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{recharge_amount} BDT Recharge Successful to {mobile_number}")
                else:
                    print("Please enter valid pin")
            else:
                print("Please enter valid recharge amount")
        else:
            print("Please enter valid number")
    else:
        print("please choose a valid option")
elif choice==4:
    merchant_number = int(input("Enter merchant number: "))
    if merchant_number:
        amount=int(input("Enter amount: "))
        if amount:
            pin = int(input("Enter pin: "))
            if pin:
                print(f"{amount} BDT Payment Successful to {merchant_number}")
            else:
                print("Please enter valid pin")
        else:
            print("Please enter valid amount")
    else:
        ("Please enter valid number")
elif choice==5:
    from_whom = int(input('''
Choose an option:
1. From Agent
2. From ATM
3. Priyo Agent Numbers
    '''))
    if from_whom:
        num= int(input("Enter number: "))
        if num:
            amount=int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Cash Out Successful to {num}")
                else:
                    print("Please enter valid pin")
            else:
                print("Please enter valid amount")
        else:
            print("Please enter valid number")
    else:
        print("please choose a valid option")
elif choice==6:
    bill_type = int(input('''
Choose an option:
1. Electricity (Prepaid)
2. Electricity (Postpaid)
3. Gas
4. Water
5. Internet & Phone
6. TV
7. City Services
8. Education
9. Financial Services
10. Others
    '''))
    bill_number = int(input("Enter bill number: "))
    if bill_number:
        if bill_number:
            amount=int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Pay Bill Successful to {bill_number}")
                else:
                    print("Please enter valid pin")
            else:
                print("Please enter valid amount")
        else:
            print("Please enter valid bill number")
    else:
        print("please choose a valid option")