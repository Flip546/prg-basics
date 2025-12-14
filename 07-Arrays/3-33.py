array = [
[3,2,4,5,6],
[2,8,6,9,2],
[1,9,0,5,4]
]

firstcol= array[0][0], array[1][0], array[2][0]
lastcol = array[0][-1], array[1][-1], array[2][-1]
(array[0][0], array[1][0], array[2][0]), (array[0][-1], array[1][-1], array[2][-1])  = (array[0][-1], array[1][-1], array[2][-1]),(array[0][0], array[1][0], array[2][0])

for i in array:
    print(*i)