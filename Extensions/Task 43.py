import random

numbers = [0,0,0,0,0,0]

for i in range(100):
    result = random.randint(1,6)
    result = result - 1
    
    so_far = numbers[result] + 1
    numbers[result] = so_far

for i in range(6):
    string = f"{i+1}: "
    for j in range(numbers[i]):
        string = f"{string}|"

    print(f"{string:<10} - {numbers[i]}")