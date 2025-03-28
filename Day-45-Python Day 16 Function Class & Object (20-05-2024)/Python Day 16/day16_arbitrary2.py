# print all child name in single line
def my_function(*names):
    print("The youngest child are:",end=" ")
    for x in names:
        if x == names[-1]:
            print(x,end=".")
        else:
            
            print(x,end=",")

my_function("Emil","Tobias","Linus")