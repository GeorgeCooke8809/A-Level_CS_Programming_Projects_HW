def sort(in_list):
    ordered_list = in_list
    length = len(in_list)

    for i in range(length-1):
        current = in_list[i+1]
        sorted = False
        index = 0

        while sorted == False:
            if in_list[index].upper() > current.upper():
                ordered_list.pop(i+1)
                ordered_list.insert(index, current)
                sorted = True
            elif in_list[index].upper() == current.upper():
                ordered_list.pop(i+1)
                ordered_list.insert(index, current)
                sorted = True
            elif in_list[index].upper() < current.upper():
                index += 1

    return ordered_list

names = []
running = True
index = 1

while running:
    name = input(f"Name {index}: ")
    if name.upper() == "EXIT":
        running = False
    else:
        names.append(name)
    
    index += 1

names = sort(names)
names_string = f"Ordered Names: {names[0]}"

for i in range(len(names)-1):
    names_string = f"{names_string}, {names[i+1]}"
print(f"\n{names_string}")