fruits = [['alahi','almin','tansen'],'banana','cherry']
for x in fruits:
    if isinstance(x, list):  # Check if the item is a list
        for i in x:
            print(i)
    else:
        print(x)
