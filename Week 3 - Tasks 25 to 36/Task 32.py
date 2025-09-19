def sort(names):
    pass
    #TODO: Finish this function

names = []

for i in range(3):
    name = input(f"Name {i+1}: ")
    names.append(name)

ordered_names = sort(names)

for i in range(3):
    print(f"Ordered Name {i+1}: {ordered_names[i]}")