prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
cart = {'juice': 3, 'bread': 1, 'milk': 2}
total = 0
for i in cart:
    if i in prices:
        total += cart[i] * prices[i]
print(f'Total amount value of products in cart: {total}')

