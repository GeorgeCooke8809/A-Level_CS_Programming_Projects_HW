age = int(input("Age: "))
licence = input("Do You Have A Drivers Licence (Y/N): ")

if licence.upper() == "Y":
    licence = True
elif licence.upper() == "N":
    licence = False

if age > 21 and licence == True:
    print("You can drive the mini bus.")
else:
    print("You cannot drive the mini bus.")