# Fibonacci series
user_input = 10
a = 0
b = 1
fibonacci = []
for i in range(user_input):
    fibonacci.append(a)
    next_number = a + b
    a = b
    b = next_number
print(fibonacci)
