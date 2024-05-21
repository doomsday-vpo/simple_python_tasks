BONUS_POINTS_BELOW_HUNDRED = 5
BONUS_PERCENT_OVER_HUNDRED = 20 / 100
BONUS_PERCENT_OVER_THOUSAND = 10 / 100
BONUS_POINTS_EVEN = 1
BOONUS_POINT_END_IN_FIVE = 2

points = int(input())

total_points = points
if points <= 100 :
    total_points = total_points + BONUS_POINTS_BELOW_HUNDRED

elif points > 1000:
    total_points = total_points + points * BONUS_PERCENT_OVER_THOUSAND
elif points > 100:
    total_points = total_points + points * BONUS_PERCENT_OVER_HUNDRED

if points % 2 == 0:
    total_points = total_points + BONUS_POINTS_EVEN
elif points % 10 == 5:
    total_points = total_points + BOONUS_POINT_END_IN_FIVE

print(total_points - points)
print(total_points)






