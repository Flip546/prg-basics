arr = [7, 9, 2, 4, 5, 6]
odd1 = []  # Lista na nieparzyste
even1 = [] # Lista na parzyste
final = [] # Lista końcowa

for i in arr:
    # Sprawdzamy resztę z dzielenia przez 2
    if i % 2 != 0:       # Jeśli reszta różna od 0 -> nieparzysta
        odd1.append(i)   # Dodajemy liczbę 'i' do listy 'odd1'
    else:                # W przeciwnym razie -> parzysta
        even1.append(i)  # Dodajemy liczbę 'i' do listy 'even1'

# Sortujemy obie listy
odd1.sort()
even1.sort()

# Łączymy listy (najpierw nieparzyste, potem parzyste - lub odwrotnie)
final = odd1 + even1

print("Liczby nieparzyste:", odd1)
print("Liczby parzyste:", even1)
print("Wynik końcowy:", final)