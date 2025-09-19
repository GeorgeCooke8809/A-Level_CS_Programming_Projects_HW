def change(bill, given):
    change = given - bill

    return ("%.2f" % change)

print(f"£{change(bill = 8.5, given = 10)}")
