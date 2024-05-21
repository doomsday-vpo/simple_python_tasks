#contstant price
puzzle_price = 2.60
doll_price = 3
teddybear_price = 4.10
minion_price = 8.20
truck_price = 2
#discounts
DISCOUNT_OVER_FIFTY = 25/100
RENT_PERCENT = 10/100
DISCOUNT_ABOVE_QTY = 50

#inputs
holiday_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddybear_count = int(input())
minions_count = int(input())
trucks_count = int(input())

subtotal = puzzle_count * puzzle_price\
           + dolls_count * doll_price \
           + teddybear_count * teddybear_price + minions_count*minion_price + trucks_count*truck_price

item_qty = puzzle_count + dolls_count + teddybear_count + minions_count + trucks_count

grand_total = subtotal
if item_qty >= DISCOUNT_ABOVE_QTY:
    grand_total = subtotal - subtotal*DISCOUNT_OVER_FIFTY

remaining_money = grand_total - grand_total*RENT_PERCENT

if holiday_price <= remaining_money:
    money_after_holiday = remaining_money - holiday_price
    print(f"Yes! {money_after_holiday:0.2f} lv left.")

else:
     money_needed = holiday_price - remaining_money
     print(f"Not enough money! {money_needed:0.2f} lv needed.")

