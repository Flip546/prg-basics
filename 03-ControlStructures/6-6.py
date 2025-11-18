while True:
    # 1. Bezpieczne pobranie danych z obsługą błędów (ValueError)
    try:
        # Pytamy użytkownika, upewniając się, że wejście to liczba całkowita
        Hours = int(input('Enter number of hours that car will be on parking: '))
    except ValueError:
        # Wypisuje błąd, jeśli użytkownik wpisał tekst/znak
        print("Błąd: Proszę wprowadzić poprawną LICZBĘ całkowitą.")
        continue # Wracamy na początek pętli

    # 2. Obsługa przypadków godzin (np. 0 lub ujemne)
    if Hours <= 0:
        print("Liczba godzin musi być większa niż zero (lub wprowadź 0, aby wyjść).")
        # Jeśli chcesz, aby 0 kończyło program, użyj:
        # if Hours == 0:
        #     break
        continue # Wracamy na początek pętli
        
    # 3. Logika cennika
    
    # Krok 1: Płatność za 1 do 2 godzin (Włącznie z 1 i 2)
    if 1 <= Hours <= 2:
        print("You need to pay 5 PLN.")
        break
        
    # Krok 2: Płatność za 3 do 6 godzin (Włącznie z 3 i 6)
    elif 3 <= Hours <= 6:
        print("You need to pay 15 PLN.")
        break
        
    # Krok 3: Płatność za powyżej 6 godzin
    elif Hours > 6:
        print("You need to pay 20 PLN.")
        break