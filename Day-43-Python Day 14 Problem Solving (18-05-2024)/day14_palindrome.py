# palindrome check
myDigit=323
digit_str=str(myDigit)
digit_reverse=""
for i in range(len(digit_str)):
    index=i+1
    digit_reverse += digit_str[-index]
if int(digit_reverse) == myDigit:
    print("It is a Palindrome number")
print(f"Original digit: {myDigit}")
print(f"Reverse digit: {int(digit_reverse)}")