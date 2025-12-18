tekst = "Jestem swietnym gosciem i kocham gotowac kluski oraz kocham sport"

# 1. Zamieniamy tekst na małe litery i dzielimy na listę słów
slowa = tekst.lower().split()

# 2. Tworzymy pusty słownik na wyniki
licznik = {}

# 3. Przechodzimy przez każde słowo w liście
for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] += 1  # Jeśli słowo już jest w słowniku, zwiększamy licznik
    else:
        licznik[slowo] = 1   # Jeśli słowa nie ma, dodajemy je z wartością 1

# 4. Wyświetlamy wynik
for slowo, ile in licznik.items():
    print(f"Słowo '{slowo}' występuje {ile} razy")