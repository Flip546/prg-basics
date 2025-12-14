arr1 = [1, 3, 4 ]
arr2 = [ 3, 4 , 3]
count  = 0
for i in arr1:
    if i in arr2:
        count += 1
if count == len(arr1):
        print('Jest podzbiorem')
else:
     print('Nie, brakuje elementów')



