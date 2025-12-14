def create_2d_arr(x, y):
    """
    Tworzy tablicę 2D o wymiarach x (wiersze) na y (kolumny),
    wypełnioną zerami.
    """
    # Używamy tzw. "list comprehension", aby stworzyć niezależne wiersze
    tablica = [[0 for _ in range(y)] for _ in range(x)]
    return tablica

# Tworzenie tablicy o wymiarach 3 na 5 (3 wiersze, 5 kolumn)
moja_tablica = create_2d_arr(3, 5)

# Wyświetlenie całej tablicy (jako lista list)
print(moja_tablica)

# Opcjonalnie: Wyświetlenie w ładniejszy sposób (wiersz pod wierszem)
print("\nŁadniejszy podgląd:")
for wiersz in moja_tablica:
    print(*wiersz)