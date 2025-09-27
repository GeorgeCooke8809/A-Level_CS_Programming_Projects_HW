while True:
    number = int(input("Number: "))
    current = 2
    running = True

    while running and current < number:
        if number % current == 0: # Is divisible
            print(f"{number} is not prime.\n")
            running = False
        else:
            current += 1

    if running == True: # Triggers when current reaches number and divisible index has not been found
        print(f"{number} is prime.\n")