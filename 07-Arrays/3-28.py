array = [
[7, 3, 7 ,9 ,0],
[2 ,9 ,0 ,1 ,5],
[3 ,8, 6, 4, 7],
[8 ,7 ,1, 1 ,5]
]

count = 0
suma = 0
for wiersz in array:
 count += 1
 for liczba in wiersz:
  if count == 4:
   suma += liczba
   
  

print(suma)
  