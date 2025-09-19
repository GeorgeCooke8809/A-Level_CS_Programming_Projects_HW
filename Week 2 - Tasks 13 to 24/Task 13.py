def economy(litres, miles):
    gallons = litres / 3.78541178
    efficiency = miles / gallons

    return efficiency

print(f"Your Fuel Efficiency Is {economy(40,300):.2f} Gallons Per Mile.")
