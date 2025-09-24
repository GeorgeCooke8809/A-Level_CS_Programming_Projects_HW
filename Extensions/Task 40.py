students = []
marks = []

running = True

while running:
    name = input("Name: ")
    mark = input("Mark: ")

    if name.upper() != "EXIT" and mark.upper() != "EXIT":
        students.append(name)
        marks.append(float(mark))
    else:
        running = False

    print()

total = 0
number_students = len(students)

for i in range(number_students):
    total += marks[i]

average = total / number_students

print(f"Average: {average:.2f}\n")

for i in range(number_students):
    if marks[i] > average:
        average_state = "Above Average"
    elif marks[i] < average:
        average_state = "Below Average"
    else:
        average_state = "Average"


    print(f"{f"Student: {students[i]}":<20}{f"Mark: {marks[i]}":<20}Comparative: {average_state}")