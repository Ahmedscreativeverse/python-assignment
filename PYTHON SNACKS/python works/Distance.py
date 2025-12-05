


# user enters their driving distance

# user enters the price per gallon

# The price of driving is calculated with all these values


#price = (driving_distance / mile_per_gallon) * price_per_gallon




driving_distance = float(input("Enter the distance to drive (miles): "))

mile_per_gallon = float(input("Enter your car's miles per gallon (MPG): "))

price_per_gallon = float(input("Enter the price per gallon ($): "))

price = (driving_distance / mile_per_gallon) * price_per_gallon


print(f"The price of your trip is: ${price:.2f}")

