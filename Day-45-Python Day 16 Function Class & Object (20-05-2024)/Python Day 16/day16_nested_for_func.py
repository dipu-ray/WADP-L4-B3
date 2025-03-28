# print each name later individually using nested loop
def my_function(fname,lname):
    for names in fname,lname:
        print(names)
        for j in names:
            print(j)

my_function("Alahi","Tansennn")