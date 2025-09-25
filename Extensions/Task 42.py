choice = ""
running = True

while running:
    choice = input()

    if len(choice) <= 36:
        running = False
    else:
        print("That string is too long, please try again.")

choice = list(choice)

index = 0
character_array = []

for i in range(6):
    try: 
        character_array.append(choice[index:index + 6])
    except: # List out of range - doesn't matter
        pass

    index += 6

final_array = []

for i in range(6):
    temp_string = ""
    for j in range(6):
        try:
            temp_string = f"{temp_string}{character_array[j][i]}"
        except:
            pass
    final_array.append(temp_string)

for i in range(6):
    print(final_array[i])