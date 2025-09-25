def main():
    choice = getNumber()
    return factorial(choice)

def getNumber():
    user_input = int(input("Choice: "))

    return user_input

def factorial(number):
    multiplier = number
    total = 1

    while multiplier > 0:
        total = total * multiplier
        multiplier -= 1

    return total

print(f"The factorial is {main()}")
# The use of functions here is so inefficient, I don't see why you're making me do it.