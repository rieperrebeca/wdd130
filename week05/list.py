
# print the questions
print = ("Welcome to the Shopping Cart Program!")
print = ("Please select one of the following:")
print = ("1. Add item")
print = ("2. View cart")
print = ("3. Remove item")
print = ("4. Compute total")
print = ("5. Quit")

list = []

action = None

while action != "quit":
    action = input("Please enter an action:")
    
    if action != "quit":
        list.append(action)
