Number = int(input('Enter amount of money:'))
zloty5 = 5
zloty1 = 1
zloty2 = 2
count5 = Number // zloty5
rest = Number % zloty5
count2 = rest // zloty2
rest2 = rest % zloty2
count1 = rest2 // zloty1
print(f'Number of coins 5zl:{count5}, 2zl:{count2}, 1zl: {count1}')
