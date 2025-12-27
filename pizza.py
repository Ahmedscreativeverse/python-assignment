

import math



print("""
Pizza type          Number of Slices      Price per Box
Sapa size                4                   2,000
Small money              6                   2,400
Big boys                 8                   3,000
Odogwu                   12                  4,200
""")



number_of_guest = int(input("Enter the number of guest: "))
pizza_type = input("Enter the pizza type: ")

match pizza_type:
    case "Sapa size":
        number_of_slices = 4
        price = 2000
    
    case "Small money":
        number_of_slices = 6
        price = 2400  
    
    case "Big boys":
        number_of_slices = 8
        price = 3000  
    
    case "Odogwu":
        number_of_slices = 12
        price = 4200

boxes_of_pizza_to_buy = math.ceil(number_of_guest / number_of_slices)
leftover_slices = (boxes_of_pizza_to_buy * number_of_slices) - number_of_guest
total_price = boxes_of_pizza_to_buy * price

print(f"Number of boxes of pizza to buy = {boxes_of_pizza_to_buy} boxes")
print(f"Number of leftover slices after serving = {leftover_slices} slices")
print(f"Price = {total_price}")
