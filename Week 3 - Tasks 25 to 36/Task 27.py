def finish_time(start, taken):
    finish_hours = int(start[0]) + int(taken[0])
    finish_minutes = int(start[1]) + int(taken[1])

    if finish_minutes > 60:
        finish_minutes -= 60
        finish_hours += 1

    if finish_hours > 24:
        finish_hours -= 24

    return f"You will finish your journey at {finish_hours:02}:{finish_minutes:02}"

start_time = input("Start Time (hh:mm): ")
start_time = start_time.split(":")

time_taken = input("Time Taken (hh:mm): ")
time_taken = time_taken.split(":")

print(finish_time(start_time, time_taken))