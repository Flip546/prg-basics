###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))
def triangle_area(a,b,c):
    s = (a + b +c )/2
    result = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return result

area1 = triangle_area(a,b,c)


print(f'The area of ​​a triangle with sides 3,4,5 is {result}')
print(f'The area of ​​a triangle with sides 5,12,13 is {triangle_area}')
print(f'The area of ​​a triangle with sides 7,24,25 is {triangle_area}')