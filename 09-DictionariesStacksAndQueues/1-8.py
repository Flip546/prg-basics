price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
totalval = 0
print('ITEM LIST BEFORE DISCOUNT:')
for i,j in price_list.items():
    totalval += j
    print(i,j)

print(f'Total value before discount: {round(totalval, 2)}')
total = 0
for a,h in price_list.items():
    h = h * 0.9
    total += h
    print(a,round(h,2))
print(f'TOTAL VALUE AFTER DISCOUNT: {round(total,2)}')
    
