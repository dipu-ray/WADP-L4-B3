# Digit reverse
myDigit=324345
digit_str=str(myDigit)
digit_reverse=""
for i in range(len(digit_str)):
    index=i+1
    digit_reverse += digit_str[-index]

print(f"Original digit: {myDigit}")
print(f"Reverse digit: {int(digit_reverse)}")