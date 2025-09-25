names = ["Peter", "James", "Martin", "Akil", "George"]

search = input("Search: ")

index = names.index(search)

if index == None:
    print("That is not in the list.")
else:
    print(f"That is at spot {index} in the list.")