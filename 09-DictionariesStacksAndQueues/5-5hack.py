from collections import Counter

tekst = "Jestem swietnym gosciem i kocham gotowac kluski oraz kocham sport"
licznik = Counter(tekst.lower().split())

print(licznik)
# Wynik: Counter({'kocham': 2, 'jestem': 1, 'swietnym': 1, ...})