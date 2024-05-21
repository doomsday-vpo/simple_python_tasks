first_one = int(input())
second_one = int(input())
third_one = int(input())

sum_seconds = first_one + second_one + third_one

minutes = sum_seconds // 60
seconds = sum_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
