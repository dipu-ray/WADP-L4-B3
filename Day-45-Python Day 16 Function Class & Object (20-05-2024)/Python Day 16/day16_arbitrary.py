# Arbitrary *kwargs
def my_function(*names):
    print(type(names))
    print(list(names))

my_function("Mango","Orange")