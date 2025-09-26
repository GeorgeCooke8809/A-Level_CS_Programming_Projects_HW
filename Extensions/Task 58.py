correct = False
y_correct = False
m_correct = False
d_correct = False

while correct == False:
    while not y_correct:
        try:
            year = int(input("Year of Birth: "))
            if year >= 1915 and year <= 2025:
                y_correct = True
            else:
                print("That is not a valid year.")
        except:
            print("That is not a number.")
    while not m_correct:
        try:
            month = int(input("Month of Birth: "))
            if month >= 1 and month <= 12:
                m_correct = True
            else:
                print("That is not a valid month.")
        except:
            print("That is not a number.")
    while not d_correct:
        try:
            day = int(input("Day of Birth: "))
            if day >= 1 and day <= 31:
                d_correct = True
                correct = True
            else:
                print("That is not a valid day.")
        except:
            print("That is not a number.")

print(f"Your date of birth has been validated at {day}/{month}/{year}")