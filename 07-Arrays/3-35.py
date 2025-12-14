def transpose_matrix(m):
    # zip(*m) bierze wiersze i łączy ich pierwsze elementy, potem drugie itd.
    # map(list, ...) zamienia wynik z powrotem na listę
    return [list(row) for row in zip(*m)]

# Działa tak samo, a zajmuje jedną linijkę!

print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))
    

        
