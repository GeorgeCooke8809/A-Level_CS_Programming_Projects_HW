entered = False

while not entered:
    choice = input("Password: ")
    if choice == "secret":
        entered = True
    else:
        print("That is not correct, please try again.\n")

print("That is correct, well done.")