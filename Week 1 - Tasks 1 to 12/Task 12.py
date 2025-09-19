def toCentigrade(fahrenheit):
    centigrade = (5*(fahrenheit-32))/9
    #DEBUGGING - 7print(centigrade)
    return centigrade

f = float(input("Temperature (F): "))
celcius = toCentigrade(f)
print(f"Temperature (C): {"{0:,.2f}".format(celcius)}")
