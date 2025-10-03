amount = int(input("Go Up To: "))

string = ""

for i in range(amount):
    string = f"{string:<4}{i+1:<4}"

print(string)

for i in range(amount):
    string = f"{i+1:<4}"
    for j in range(amount):
        string = f"{string}{(i+1)*(j+1):<4}"

    print(string)