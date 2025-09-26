limit = int(input("Limit: "))

sequence = [1, 1]
last1 = 1
last2 = 1

while last1 + last2 < limit:
    new = last1 + last2
    last2 = last1
    last1 = new
    sequence.append(new)

string = ""

for i in sequence:
    string = f"{string}{i} "

print(string)
print(f"There are a total of {len(sequence)} items in the sequence before {limit}.")