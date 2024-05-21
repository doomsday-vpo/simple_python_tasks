speed = float(input())

if speed <= 10:
    print("slow")
if 10 < speed <= 50:
    print("average")
if 50 < speed <= 150:
    print("fast")
if 150 < speed <= 1000:
    print("ultra fast")
if speed > 1000:
    print("extremely fast")


speed_limit = float(input())

if speed_limit <= 10:
    print("slow")
elif speed_limit <= 50:
    print("average")
elif speed_limit <= 100:
    print("fast")
elif speed_limit <= 150:
    print("ultra fast")
elife speed_limit