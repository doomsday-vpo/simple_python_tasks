hours = int(input())
minutes = int(input())

next_minutes = minutes + 15
next_hours = hours
if next_minutes >= 60:
    next_hours = hours + 1
    next_minutes = next_minutes - 60

result_hours = str(next_hours)
results_minutes = str(next_minutes)
if next_minutes < 10:
    results_minutes = "0" + str(next_minutes)
if next_hours >= 24:
   result_hours =  str(next_hours -24)

print(f"{result_hours}:{results_minutes}")