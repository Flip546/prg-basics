PRICE = input('Enter price: ')
PRICE = float(PRICE)
Discount = input('Enter discount in %: ')
Discount = float(Discount)
A = PRICE * Discount/100 
B = PRICE - A
print(f'Price with discount:{B}')
Diffrence = PRICE - B 
print(f'Diffrence bettwen prices is:{Diffrence}')