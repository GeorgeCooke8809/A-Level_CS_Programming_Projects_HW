f = open("names.txt", "r+")

running = True
seek = 0
line = " "

while running:
    if line != "":
        line = f.readline()
        line = line.replace("\n", "")
        print(f"{line}")
    else:
        running = False

print("End of document.")