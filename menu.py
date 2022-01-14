# import를 사용하지 않으면 name 'random' is not define error가 뜬다.
import random

menu = ['Pizza', 'Pasta', 'soup', 'mac', 'kfc']

# I select menu on the 'menu' list
#random.choice(menu)

today_menu = random.choice(menu)

print(today_menu)