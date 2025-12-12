class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def parimeter(self):
      return self.a * 4
square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {Square(4).area}, Perimeter is {Square(4).parimeter} ')
print (F'Square with side 6: {square2.area , square2.parimeter}')
