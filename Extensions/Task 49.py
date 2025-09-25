vat = 0.15

original = float(input("Original Total: £"))
vat_cost = original * vat
new = original + vat_cost

print(f"VAT Cost: £{vat_cost:.2f}\nOriginal Cost: £{original:.2f}\nNew Total: £{new:.2f}")