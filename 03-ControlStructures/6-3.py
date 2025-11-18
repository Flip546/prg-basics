###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
onof = int(input('Which switch turn on?:(1,2)?: '))
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0

if onof==1:
    light_switch1 = True
    bulbs_on += 1
elif onof==2:
    light_switch2 = True
    bulbs_on += 2
else:
    print("Podano nieprawidłowe wartości.")


 
print(f'There are currently  {bulbs_on} bulbs on in the house.')