base = 3.5
prices = []

for i in range(11): # Surely this is the least efficient way of doing this? Why did you make me?
    price = base + (0.82 * i)
    prices.append(price)

running = True

while running:
    choice = int(input("Dividers Wanted (Up To 10): "))
    if choice <= 10:
        print(f"That will cost at total of £{prices[choice]:.2f}\n")
        again = input(f"Would you like to go again (Y/N)? ").upper()

        if again == "N":
            running = False
    else:
        print("That is not a valid number of cases. Please try again.")