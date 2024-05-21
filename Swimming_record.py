import math

SLOW_EVERY_X_METERS = 15

SLOW_BY = 12.5

current_record = float(input())
distance = float(input())
time_per_meter = float(input())

time_to_swim = distance * time_per_meter
slow_down_count = distance / SLOW_EVERY_X_METERS
slow_down_count = math.floor(slow_down_count)

total_time_swimming = time_to_swim + slow_down_count * SLOW_BY

if total_time_swimming < current_record:
    print(f" Yes, he succeeded! The new world record is {total_time_swimming:.2f} seconds.")
else:
    seconds_short = total_time_swimming - current_record
    print(f"No, he failed! He was {seconds_short:.2f} seconds slower.")