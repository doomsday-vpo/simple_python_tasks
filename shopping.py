DISCOUNT_PERCENT = 15 / 100
VIDEO_CARD_PRICE = 250
CPU_PRICE_PERCENT = 35 / 100
RAM_PRICE_PERCENT = 10 / 100

budget = float(input())
video_cards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

total_video_card_price = video_cards_count * VIDEO_CARD_PRICE
single_cpu_price = total_video_card_price * CPU_PRICE_PERCENT
total_cpu_price = single_cpu_price * cpu_count

single_ram_price = total_video_card_price * RAM_PRICE_PERCENT
total_ram_price = ram_count * single_ram_price

subtotal = total_video_card_price + total_ram_price + total_cpu_price
grandtotal = subtotal
if video_cards_count > cpu_count:
    grandtotal = subtotal - subtotal * DISCOUNT_PERCENT

if budget >= grandtotal:
    remaining_budget = budget - grandtotal
    print(f"You have {remaining_budget:.2f} leva left!")
else:
    money_needed = grandtotal - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")