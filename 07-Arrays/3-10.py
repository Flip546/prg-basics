arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

wynik = []

for numer in arr1:

    if numer not in arr2:
        wynik.append(numer)

print(wynik)