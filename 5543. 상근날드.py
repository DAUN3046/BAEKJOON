s_burger_price = int(input()) #sangdeok burger price
j_burger_price = int(input()) #joongdeok burger price
h_burger_price = int(input()) #hadeok burger price
cola_price = int(input()) #cola price
cider_price = int(input() )#cider price

burger_price = [s_burger_price, j_burger_price, h_burger_price]
drink_price = [cola_price, cider_price]

print(min(burger_price) + min(drink_price) - 50)