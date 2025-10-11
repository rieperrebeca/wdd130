
cart = []

# print the questions
print("Welcome to the Shopping Cart Program!")
print("")

#loop
while True:

    print("\nPlease select one of the following:")
    print("")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

#choice
    action = input("Please enter an action: ")
    print("")

    if action == "1":
        name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{name}'? $"))
        cart.append([name, price])
        print(f"'{name}' has been added to the cart at ${price:.2f}.")

    elif action == "2":
        print("The contents of the shopping cart are:")
        if len(cart) == 0:
            print("The cart is empty.")
            print("")
        else:
            for item in cart:
                print(item)
                print("")

    elif action == "3":
        print("Remove item not available in milestone.")
        print("")

    elif action == "4":
        print("Compute total not available in milestone.")
        print("")

    elif action == "5":
        print("Thank you. Goodbye.")
        print("")
        break

    else:
        print("Invalid option. Please choose between 1 and 5.")
        print("")
    

