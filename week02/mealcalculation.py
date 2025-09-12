#ask for the information

child_meal = float(input("What is the price of a child's meal?"))
adult_meal = float(input("What is the price of an adult's meal?"))
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))
drink_price = float(input("What is the price of drinks?"))
drink = int(input("How many drinks were ordered?"))

#calculate the value
subtotal = (child_meal * children) + (adult_meal * adults) + (drink_price * drink)
tax = subtotal * 3.5
total_with_tax = subtotal + tax
total_with_tax_and_tip = total_with_tax * 1.5

#display the value
print("")
print(f"Subtotal ${subtotal}")
print("")
print(f"The total cost of the meal with tax is: ${total_with_tax}")
print("")
print(f"The total cost of the meal with tax is and tip is: ${total_with_tax_and_tip}")

#change calculation
payment = float(input("What is the payment amount?"))
change = payment - total_with_tax
print(f"The change due is: ${change}")
