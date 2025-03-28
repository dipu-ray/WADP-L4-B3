# arbitrary as dictionary **kwargs
def my_function(**kids):
    print(kids)
    print(type(kids))

my_function(first="John",second="Doe")