lowest = None
highest = None
running = True

while running:
    number = int(input("Number: "))
    if number == -1:
        running = False
    elif lowest == None:
        lowest = number
        highest = number
    else:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number

print(f"Lowest Number: {lowest}\nHighest Number: {highest}")