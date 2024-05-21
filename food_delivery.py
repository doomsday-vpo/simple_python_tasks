CHICkEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETERIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50
DESSERT_PRICE_RATE = 20/100


chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

chicken_menu_total = chicken_menu * CHICkEN_MENU_PRICE
fish_menu_total = fish_menu * FISH_MENU_PRICE
vegeterian_menu_total = vegeterian_menu * VEGETERIAN_MENU_PRICE
subtotal = chicken_menu_total + fish_menu_total + vegeterian_menu_total
dessert_total = subtotal * DESSERT_PRICE_RATE
grand_total = subtotal + dessert_total + DELIVERY_PRICE

print(grand_total)

