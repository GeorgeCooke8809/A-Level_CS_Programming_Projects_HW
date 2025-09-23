def names_array(names):
    for i in names:
        print(i)

names = []

for index in range(4):
    name = input(f"Name {index + 1}: ")
    names.append(name)

names_array(names)