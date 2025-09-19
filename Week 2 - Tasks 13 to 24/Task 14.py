def coach(members, capacity):
    full = members // capacity
    last = members % capacity

    return (full, last)

members = int(input("Members: "))
capacity = int(input("Coach Capacity: "))

coach_data = coach(members, capacity)

print(f"There will be {coach_data[0]} full coaches and the last coach will have {coach_data[1]} people on it.")
