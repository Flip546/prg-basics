###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#Enter the temperature
Cel = float(input('Enter the temparature in Celsius: '))
Far = Cel *(9/5) +32
Kel = Cel + 273.15
print(f'Temperature in Fahrenheit is {Far} and in Kelvin is {Kel}')
