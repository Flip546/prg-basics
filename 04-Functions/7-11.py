def f(n1,n2,n3):
   return n1 < 0 or n2 < 0 or n3 < 0



print(f(1, 2, 3) )     # False
print(f(-1, 2, 3) )   # True
print(f(1, -2, 3) )    # True
print(f(1, 2, -3) )    # True
