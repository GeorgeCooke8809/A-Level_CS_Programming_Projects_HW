first = list(input("Word 1: ").upper())
second = list(input("Word 2: ").upper())

passing = True

for i in first:
    if i in second:
        index = second.index(i)
        second.pop(index)
    else:
        passing = False

if passing:
    print("You can make the first word from the second.")
else:
    print("You can't make the first word from the second.")