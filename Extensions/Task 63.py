string = list(input("Plain Text: "))
previous = string[0]
count = 0
final = string [0]

for i in string:
    if i == previous:
        count += 1
    else:
        final = f"{final} {count} {i}"
        count = 1

    previous =  i

final = f"{final} {count}"
print(f"Compressed Text: {final}")