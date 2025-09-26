running = True
while running:
    try:
        distance = int(input("Distance (miles): "))
        running = False
    except:
        print("That is not a valid distance.")

running = True
while running:
    try:
        time = int(input("Time (minutes): "))
        running = False
    except:
        print("That is not a valid time.")

print(f"You ran an average of a {time/distance:.2f} minute mile.")