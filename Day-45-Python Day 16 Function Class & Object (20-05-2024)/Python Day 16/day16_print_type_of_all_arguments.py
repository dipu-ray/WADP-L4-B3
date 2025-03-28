# print type of all arguments
def my_function(**food):
    # for key, value in food.items():
    #     print(f"Type: {type(value)}")
    #     print(value)
    for key, value in food.items():
        print(f"Type: {type(value)}")
        print(value)

food_list=["Mango","Orange","Apple"]
food_tuple=("Mango","Orange","Apple")
food_set={"Mango","Orange","Apple"}
food_dict={"food1":"Mango","food2":"Orange","food3":"Apple"}

my_function(food_list=food_list)
my_function(food_tuple=food_tuple)
my_function(food_set=food_set)
my_function(food_dict=food_dict)