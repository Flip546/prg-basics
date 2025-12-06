
lista = [1, 2, 3, 2, 4, 5, 5, 1, 6]

widziane = set()
powtorki = set()

for liczba in lista:
    if liczba in widziane:
        powtorki.add(liczba)
    else:
        widziane.add(liczba)

print("Powtarzające się liczby:", *powtorki)
