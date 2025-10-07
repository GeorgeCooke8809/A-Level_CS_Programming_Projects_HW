age = int(input("Age: "))
licence = input("Do You Have A Drivers Licence (Y/N): ")
if age > 21 and licence.upper() == "Y": print("You can drive the mini bus.")
else: print("You cannot drive the mini bus.")