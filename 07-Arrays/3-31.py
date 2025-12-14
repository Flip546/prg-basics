array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
maks = array[0][0]
max_row = 0
max_col = 0

# range(len(array)) generuje: 0, 1, 2, 3
for i in range(len(array)):
    # range(len(array[i])) generuje: 0, 1 dla każdego wiersza
    for j in range(len(array[i])):
        if array[i][j] > maks:
            maks = array[i][j]
            max_row = i # Zapamiętaj aktualny wiersz
            max_col = j # Zapamiętaj aktualną kolumnę

print(f'Największa jest {maks} (rząd: {max_row}, kolumna: {max_col})')