def taxes(gross):
    tax = gross * 0.25
    net = gross - tax

    return [tax, net]

print(f"Tax: £{"{0:,.2f}".format((taxes(375))[0])}")
print(f"Net: £{"{0:,.2f}".format((taxes(375))[1])}")
