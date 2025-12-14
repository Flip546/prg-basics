
import matplotlib.pyplot as plt

x = []
y = []

# create x values (tworzenie wartości x)
# range(-100, 101) generuje liczby od -100 do 100 włącznie
for n in range(-100, 101):
    x = x + [n]

# create y values (tworzenie wartości y)
# Obliczamy funkcję f(x) = x^2 - 3 dla każdego punktu
for n in x:
    # Wzór: n do potęgi 2 minus 3
    wartosc = n**2 - 3
    y = y + [wartosc]

# print chart (rysowanie wykresu)
plt.plot(x, y)
plt.show()