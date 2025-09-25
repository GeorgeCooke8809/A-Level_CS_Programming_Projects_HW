f = open("names.txt", "a+")

for i in range(10):
    name = input()
    f.write(f"{name}\n")

f.close()