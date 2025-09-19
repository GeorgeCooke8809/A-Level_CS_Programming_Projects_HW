def check_age(age):
    if age <= 15:
        return "You are too young to drive"
    elif age == 16:
        return "You can drive this year"
    elif age >= 17 and age <= 65:
        return "You are old enough to drive"
    elif age >= 66 and age <= 75:
        return "You need to renew your licence periodically"
    else:
        return "You need to renew your licence annually"
    

while True:
    age = int(input("Age: "))
    print(check_age(age))