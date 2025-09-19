def change(bill):
    ten = ("%.2f" % (bill * 1.1))
    twelve = ("%.2f" % (bill * 1.125))

    return [ten, twelve]

print(f"10% Tip: £{(change(87))[0]}")
print(f"12.5% Tip: £{(change(87))[1]}")
