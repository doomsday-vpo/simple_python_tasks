NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
ACETONE_PRICE = 5.0
NYLON_BUFFER = 2
PAINT_BUFFER = 10/100
BAGS = 0.40
LABOUR_PRICE = 30/100

nylon = int(input())
paint = int(input())
acetone = int(input())
labour_hours = int(input())

nylon_total = (nylon + NYLON_BUFFER) * NYLON_PRICE
paint_total = (paint + (paint * PAINT_BUFFER)) * PAINT_PRICE
acetone_total = acetone * ACETONE_PRICE

total = nylon_total + paint_total + acetone_total + BAGS

price_per_hour = total * LABOUR_PRICE
price_for_labour = labour_hours * price_per_hour

total_price = total + price_for_labour
print(total_price)

