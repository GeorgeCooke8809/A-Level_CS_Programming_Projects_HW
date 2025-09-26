f = open("books.bin", "a+")

questions = ["Name: ", "ISBN: ", "Price: £", "Release Year: "]

for i in questions:
    f.write(f"{input(f"{i}")}\n")

f.close()