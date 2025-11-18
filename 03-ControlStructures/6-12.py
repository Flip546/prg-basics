number_prod = int(input('Number of the products purchased: '))
price = float(input('Price per product: '))
price_total = 0
if number_prod <= 2:
    price_total =  price * number_prod
else:
    price_total = price * 2 + (number_prod -2) * price * 0.75
print(f'Total price to pay: {price_total} PLN')