# Tworzymy tablicę dwuwymiarową 2x4 (2 wiersze, 4 kolumny)
tablica = [
    [7, 3, 7, 9],
    [2, 9, 0, 1]
]

# Program drukujący wartości w wierszach i kolumnach
# Zewnętrzna pętla leci po wierszach
for wiersz in tablica:
    # Wewnętrzna pętla leci po liczbach w danym wierszu (kolumnach)
    for liczba in wiersz:
        print(liczba, end=" ") # end=" " sprawia, że nie przeskakuje od razu do nowej linii
    print() # To print() robi pustą linię dopiero po wypisaniu całego wiersza