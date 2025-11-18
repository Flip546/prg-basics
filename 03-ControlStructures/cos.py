#
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

# Słownik mapujący liczby 1-5 na ich odpowiedniki słowne
number_to_word = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    
    # Warunek: Jeśli pozostało 5 lub mniej sekund, wyświetl słowo
    if countdown <= 5:
        # Pobieramy słowo ze słownika. Jeśli countdown jest 0, pętla się kończy
        print(number_to_word[countdown])
    else:
        # W przeciwnym razie wyświetl liczbę
        print(countdown)

    # Odliczanie i pauza
    countdown -= 1  # Poprawne odejmowanie 1 w każdej iteracji
    time.sleep(1)   # Poczekaj 1 sekundę
    
# Linijki 13, 15, 16, 17 z Twojego oryginalnego kodu zostały usunięte/poprawione.
# 13: 'countdown -= 1' było zbędne
# 15: 'if countdown <= 5:' było w złym miejscu
# 16: 'countdown -= 1' było zduplikowane

print("Time's up!")