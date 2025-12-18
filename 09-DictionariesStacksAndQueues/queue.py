
names = []
names.append('Blackie')
names.append('Whitie')
names.append('Greenie')
names.append('Silverini')

print(F'NUMBER OF ELEMENTS IN QUEUE {len(names)}')


while len(names) > 0:
    name = names.pop(0)
    print(name)