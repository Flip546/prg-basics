TEKST = input('Enter text: ')
reverse = []
for i in TEKST:
    reverse.append(i)
reverse.reverse()
for i in reverse:
    print(i,end="")

