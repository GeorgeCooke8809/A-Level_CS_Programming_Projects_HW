discounts = [[10000, 0.2], [5000, 0.15], [2500, 0.1], [1000, 0.05]]
discounted = False

ammount = float(input("Order Price: £"))

for discount in discounts:
    if discounted == False and ammount >= discount[0]:
        ammount = ammount * (1 - discount[1])
        discounted = True

print(f"Discounted Price: £{ammount:.2f}")