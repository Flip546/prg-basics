###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
a = int(a)
b = int(b)
c = int(c)
surface_cuboid = 2 * (a * b + a * c + b * c)
volume = a * b * c
print(f'The surface of cuboid is {surface_cuboid}')
print(f'Volume of the cuboid is {volume}')