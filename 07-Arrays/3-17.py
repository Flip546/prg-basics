tuple = (50,20,40,50,30,50)
print(tuple)
count = 0
value = int(input ('What number to count: '))
for i in tuple:
    if i == value:
        count += 1

print(f'Number of occurences: {count}')