def check_age(age):
    if age <= 15:
        return "You Are Entitled To A Children's Ticket"
    else:
        return "You Must Pay Full Price"
    

while True:
    age = int(input("Age: "))
    print(check_age(age))