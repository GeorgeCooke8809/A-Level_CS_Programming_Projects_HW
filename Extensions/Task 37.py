ammount = int(input("Go Up To: "))

string = ""

for i in range(ammount):
    string = f"{string:<4}{i+1:<4}"

print(string)

for i in range(ammount):
    string = f"{i+1:<4}"
    for j in range(ammount):
        string = f"{string}{(i+1)*(j+1):<4}"

    print(string)