arr = [8, 2, 5, 1, 9]

# 1. Pierwsza linijka: Napis + rozpakowana tablica
print("Array:", *arr) 

# 2. Druga linijka: Napis + pętla wyliczająca potęgi
print("2nd power:", end=" ") # Wypisz tekst i zostań w tej samej linii
for i in arr:
    print(i**2, end=" ")     # Doklejaj wynik i spację


