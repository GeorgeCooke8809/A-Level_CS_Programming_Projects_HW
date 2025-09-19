def get_grade(scores):
    total = 0

    for i in scores:
        total += i

    percent = total / 335

    if percent >= 0.8:
        return "A"
    elif percent >= 0.7:
        return "B"
    elif percent >= 0.6:
        return "C"
    elif percent >= 0.5:
        return "D"
    elif percent >= 0.4:
        return "E"
    else:
        return "U"

def check(max, component):
    passing = False
    while passing is False:
        score = int(input(f"{component} Score: "))

        if score <= max and score >= 0:
            passinig = True
            return score
        else:
            print("That is not a valid score.\n")

scores = []

scores.append(check(100, "Component 1"))
scores.append(check(60, "Component 2"))
scores.append(check(100, "Component 3"))
scores.append(check(75, "Component 4"))

print(f"Final Grade: {get_grade(scores)}")