def sort(in_list):
    ordered_list = in_list

    length = len(in_list)

    for i in range(length-1):
        current = in_list[i+1]
        sorted = False
        index = 0

        while sorted == False:
            if in_list[index] > current:
                ordered_list.pop(i+1)
                ordered_list.insert(index, current)
                sorted = True
            elif in_list[index] == current:
                ordered_list.pop(i+1)
                ordered_list.insert(index, current)
                sorted = True
            elif in_list[index] < current:
                index += 1

            return ordered_list

names = []

for i in range(3): # TODO: Make this continue until the user says stop
    name = input(f"Name {i+1}: ")
    names.append(name)

names = sort(names)

for i in range(3): # TODO: Make this print on one line
    print(f"Ordered Name {i+1}: {names[i]}")