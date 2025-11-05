# Ustawienie stałej VAT jako 0.23 (23%)
VAT_RATE = 0.23

# Pobranie kwoty od użytkownika i natychmiastowa konwersja na float (liczba z częścią dziesiętną)
amount_string = input('Enter amount: ')
amount = float(amount_string)

# Obliczenie wartości VAT
vat_amount = amount * VAT_RATE

# Obliczenie całkowitej kwoty brutto (nie wymagane przez zadanie, ale często użyteczne)
# total_amount = amount + vat_amount

# Wyświetlanie wyników z formatowaniem do dwóch miejsc po przecinku ({zmienna:.2f})

print("--- Wynik ---")
print(f"Amount : {amount:}")
print(f"VAT 23% : {vat_amount:}")