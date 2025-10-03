highest_score = 0
highest_student = ""

for i in range(5):
    current_student = input(f"Student {i+1} Name: ")
    current_score = float(input(f"{current_student} Score: "))

    if current_score > highest_score:
        highest_score = current_score
        highest_student = current_student

print(f"The best student was {highest_student} with a score of {highest_score}.")