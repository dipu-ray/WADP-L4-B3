myList = [0, 1, 2, 6, 3, 4, 3, 3, 6]
counts = {}

for item in myList:
    if item in counts:
        counts[item] += 1

    else:
        counts[item] = 1

for item, count in counts.items():
    print(f"{item}: {count}")
