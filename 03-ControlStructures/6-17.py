cordinate1 = int(input('Enter first coordinate:'))
cordinate2 = int(input('Enter first coordinate: '))
quarter = 0
if cordinate1 > 0 and cordinate2 > 0:
    quarter = 1
elif cordinate1 < 0 and cordinate2 > 0:
    quarter = 2
elif cordinate1 < 0  and cordinate2 < 0:
    quarter = 3
elif cordinate1 > 0 and cordinate2 < 0:
    quarter = 4
elif cordinate1 == 0 and cordinate2 == 0:
    quarter = 'Origin' 
print(f'The point ({cordinate1},{cordinate2}) is in quarter: {quarter}')