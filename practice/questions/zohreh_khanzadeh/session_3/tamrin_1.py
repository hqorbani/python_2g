pizza_type = input ("pizzatype= ")
number_of_pizzas = int (input ("how many pizzas do you want= "))
age = int (input ("age of people ="))


if pizza_type == ("margarita"):
    if 13<=age<=19 :
        The_final_price = number_of_pizzas * 5 -((number_of_pizzas * 5)* 5 / 100)
        print ("The_final_price:" , The_final_price)
    else:
        currency = number_of_pizzas * 5
        print ("currency:" , currency)
elif pizza_type == ("mix") :
    if 13<=age<=19 :
        The_final_price = number_of_pizzas * 6 -((number_of_pizzas * 6)* 5 / 100)
        print ("The_final_price:" , The_final_price)
    else:
        currency = number_of_pizzas * 6
        print ("currency:" , currency)
else:
    print ("Thank you for visiting our restaurant")