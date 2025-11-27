def f(x,y):
 count = 0
 x = int(x)
 y = int(y)
 for esa in range(x,y+1):
  if esa < 0 and esa % 2 == 0:
   count += 1
 return count
 
print (f(-10,10))
  