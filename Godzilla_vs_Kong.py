DECOR_PERCENT = 10 / 100
CLOTHES_DISCOUNT = 10 / 100
CLOTHES_DISCOUNT_AFTER = 150

budget = float(input())
extras = int(input())
clothes_price = float(input())

decor_price = budget * DECOR_PERCENT

extras_clothers_price = extras * clothes_price
extras_clothers_price_final = extras_clothers_price
if extras >= 150:
    extras_clothers_price_final = extras_clothers_price - extras_clothers_price * CLOTHES_DISCOUNT

total_price = decor_price + extras_clothers_price_final

if total_price <= budget:
    print("Action!")
    remaining_money = budget - total_price
    print(f"Wingard starts filming with {remaining_money:.2f} leva left.")
else:
    print("Not enough money!")
    money_needed = total_price - budget
    print(f"Wingard needs {money_needed:.2f} leva more.")

