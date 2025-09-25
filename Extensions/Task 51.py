def sort(array):
    changes_made = True

    while changes_made:
        changes_made = False
        for i in range(len(array)):
            try:
                first = array[i]
                second = array[i+1]

                if str(first).upper() > str(second).upper():
                    array[i] = second
                    array[i+1] = first
                    changes_made = True
            except:
                pass

    return array

inputting = True
collection = []

while inputting:
    choice = input()

    if choice.upper() != "EXIT":
        collection.append(choice)
    else:
        inputting = False

sorted = sort(collection)

for i in sorted:
    print(i)