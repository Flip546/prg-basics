

def rand_elem(array):
    import random
    rzecz = random.choice(array)
    return rzecz

# Testowanie
moja_lista = [2, 4, 5, 6, 2, 5, 6, 7]
wylosowany = rand_elem(moja_lista)
print(wylosowany)