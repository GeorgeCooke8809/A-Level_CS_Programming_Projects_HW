def finish_time(start_hours, start_minutes, taken_hours, taken_minutes):
    finish_hours = start_hours + taken_hours
    finish_minutes = start_minutes + taken_minutes

    if finish_minutes > 60:
        finish_minutes -= 60
        finish_hours += 1

    if finish_hours > 24:
        finish_hours -= 24

    return f"You will finish your journey at {finish_hours:02}:{finish_minutes:02}"

start_time = input("Start Time (hh:mm): ")
start_time = start_time.split(":")
start_hrs = int(start_time[0])
start_mins = int(start_time[1])

time_taken = input("Time Taken (hh:mm): ")
time_taken = time_taken.split(":")
taken_hrs = int(time_taken[0])
taken_mins = int(time_taken[1])

print(finish_time(start_hrs, start_mins, taken_hrs, taken_mins))