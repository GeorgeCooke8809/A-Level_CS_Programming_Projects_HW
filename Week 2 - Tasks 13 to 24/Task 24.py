highest_score = 0
highest_stundent = ""

for i in range(5):
    current_student = input(f"Student {i+1} Name: ")
    current_score = float(input(f"{current_student} Score: "))

    if current_score > highest_score:
        highest_score = current_score
        highest_stundent = current_student

print(f"The best student was {highest_stundent} with a score of {highest_score}.")