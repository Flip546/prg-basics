array = [1.3,2.31,3,5,6,8,9,10]
print(array)
number = float(input('Enter value to check: '))
count = 0

for i in array:
    if i > number:
        count += 1

print(f'There are {count} values greater than {number} ')
