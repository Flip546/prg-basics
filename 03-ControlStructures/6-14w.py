# 1. Pobieranie danych i zamiana od razu na True/False
# To skrócony zapis: wynik porównania (czy wpisano "yes") od razu ląduje w zmiennej
facebook = input('Do you have Facebook account? (yes/no): ') == 'yes'
twitter = input('Do you have Twitter account? (yes/no): ') == 'yes'
instagram = input('Do you have Instagram account? (yes/no): ') == 'yes'

# 2. Wyświetlenie wartości zmiennych (zgodnie z przykładem w zadaniu)
print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")

# 3. Sprawdzenie warunku "przynajmniej dwa"
# Dodajemy zmienne logiczne. Jeśli suma wynosi 2 lub więcej, warunek jest spełniony.
if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You need more social media accounts.")