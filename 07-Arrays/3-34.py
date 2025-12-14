def identity_matrix(n):
    # 1. Tworzymy macierz samych zer
    result = [[0 for i in range(n)] for i in range(n)]
    
    # 2. Wstawiamy jedynki tylko na przekątnej
    # range(n) da nam liczby 0, 1, 2...
    for i in range(n):
        result[i][i] = 1  # Wstawiamy 1 pod współrzędne [0][0], potem [1][1] itd.
        
    return result # Ważne: funkcja musi zwracać wynik!

matrix = identity_matrix(5)

# Wyświetlanie ładnie wiersz po wierszu
for row in matrix:
    print(row)