def inputs():
    towns = []
    running = True

    while running:
        town = input(f"{"Town Name":<10}: ")
        if town.upper() != "EXIT":
            population = input(f"{"Population":<10}: ")
            county = input(f"{"County":<10}: ")

            temp = [town, population, county]
            towns.append(temp)
        else:
            running = False

        print()

    return towns

database = inputs()

running = True

while running:
    choice = input("Town Search: ")

    if choice.upper() != "EXIT":
        printed = False
        for i in database:
            if choice == i[0]:
                print(f"Town: {i[0]}\nPopulation: {i[1]}\nCounty: {i[2]}\n")
                printed = True
        
        if printed == False:
            print("That town is not in the database.\n")
    else:
        running = False

running = True

while running:
    choice = input("\nCounty Search: ")

    if choice.upper() != "EXIT":
        printed = False
        for i in database:
            if choice == i[2]:
                print(f"Town: {i[0]}\nPopulation: {i[1]}\nCounty: {i[2]}\n")
                printed = True
        
        if printed == False:
            print("That county is not in the database.")
    else:
        running = False

    print()