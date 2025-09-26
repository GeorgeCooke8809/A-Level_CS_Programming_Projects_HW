questions = ["Name: ", "ISBN: ", "Price: £", "Release Year: "]

while True:
    f = open("books.bin", "a+")

    for i in questions:
        if i == "Name: ":
            f.write("\n")
        f.write(f"{input(f"{i}")}\n")

    f.close()