#ask for the information

child_meal = float(input("What is the price of a child's meal?"))
adult_meal = float(input("What is the price of an adult's meal?"))
drink_price = float(input("What is the price of drinks?"))
Snack = float(input("What is the price of a snack?"))
print("")
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))
drink = int(input("How many drinks were ordered?"))
snack_price = int(input("How many snacks were ordered?"))



#calculate the value
subtotal = (child_meal * children) + (adult_meal * adults) + (drink_price * drink) + (Snack * snack_price)
tax = subtotal * .5
total_with_tax = subtotal + tax
total_with_tax_and_tip = total_with_tax * 1.5

#display the value
print("")
print(f"Subtotal ${subtotal:.2f}")
print("")
print(f"The total cost of the meal with tax is: ${total_with_tax:.2f}")
print("")
print(f"The total cost of the meal with tax is and tip is: ${total_with_tax_and_tip:.2f}")

#change calculation
payment = float(input("What is the payment amount?"))
change = payment - total_with_tax
print("")
print(f"The change due is: ${change:.2f}")
