valid = False

while not valid:
    choice = int(input("Number: "))
    if choice >= 1 and choice <= 100:
        valid = True
    else:
        print("That is not a valid number, please enter a valid number.")

print(f"That is correct, you entered {choice}.")