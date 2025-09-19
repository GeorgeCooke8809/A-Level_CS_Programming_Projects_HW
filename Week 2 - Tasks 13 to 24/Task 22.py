import random

to_guess = random.randint(0,100)

index = 1

while index <= 5:
    guess = int(input(f"Guess {index}: "))

    if guess == to_guess:
        print("That is correct, well done!")
        index = 99 # This eliminates the need for a "guessed" variable and is more performant
    elif guess < to_guess:
        print("That's not quite right, you were a little to low. Try again.\n")
    else:
        print("That's not quite right, you were a little too high. Try again.\n")

    index += 1