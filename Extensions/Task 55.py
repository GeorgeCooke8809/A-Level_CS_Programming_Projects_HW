f = open("books.bin", "r+")

running = True
database = f.readlines()

titles = []

index = 0

for i in database:
    if i == "\n":
        try:
            print(database[index+1])
        except: # Triggers on last line
            pass
    
    index += 1