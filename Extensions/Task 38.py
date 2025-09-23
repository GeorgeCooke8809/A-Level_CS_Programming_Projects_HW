test_number = -1

while test_number < 0:
    test_number = int(input("Number: "))

count = 0
divisor = 1

while test_number > divisor:
    if test_number % divisor == 0:
        print(f"{divisor = }")
    
        count += 1
    divisor += 1

print(f"Number of Factors: {count}")