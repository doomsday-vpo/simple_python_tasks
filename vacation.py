pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = pages // pages_per_hour
hours_per_day = hours // days

print(hours_per_day)