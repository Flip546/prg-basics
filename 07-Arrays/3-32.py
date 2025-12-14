array = [
[3,2,4,5,6],
[2,8,6,9,2],
[1,9,0,5,4]
]
print('Przed: ')
for i in array:
 print(*i)
array[0], array[2] = array[2], array[0]
print('Po: ')
for i in array:
    print(*i)

