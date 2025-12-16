file_name = 'it_company.csv'

try:
    with open(file_name, 'r') as file:
        # 1. Wczytujemy wszystkie linie do listy
        lines = file.readlines()

    # 2. Pętla przeskakująca co 5 elementów (0, 5, 10, 15...)
    # range(start, stop, krok)
    for i in range(0, len(lines), 5):
        
        # Wycinamy kawałek listy od i do i+5 (czyli 5 linii)
        batch = lines[i : i+5]
        
        # Drukujemy te 5 linii
        for line in batch:
            # .strip() usuwa puste znaki (enter) z końca linii,
            # żeby print nie robił podwójnych odstępów.
            print(line.strip())
            
        # 3. Czekamy na wciśnięcie Enter
        input('Press Enter key...')

except FileNotFoundError:
    print(f"Nie znaleziono pliku {file_name}. Upewnij się, że plik istnieje.")