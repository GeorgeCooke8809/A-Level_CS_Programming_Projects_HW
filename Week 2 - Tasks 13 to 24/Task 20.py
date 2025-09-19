def get_average(list):
    total = 0
    items = 0

    for i in list:
        total += i
        items += 1

    avg = total / items
    return avg
    

number = ""
collection = []
while number != 999:
    number = int(input("Choice: "))
    collection.append(number)

print(f"Average: {get_average(collection):.2f}")