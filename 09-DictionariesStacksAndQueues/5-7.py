# Dane wejściowe
hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

# i. Funkcja zwracająca nazwy hoteli po przecinku
def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ", ".join(names)

# ii. Funkcja obliczająca średnią cenę (zaokrągloną)
def avg_price(hotels):
    total_price = 0
    for hotel in hotels:
        total_price += hotel["price"]
    
    average = total_price / len(hotels)
    return round(average)

# --- WYŚWIETLANIE WYNIKÓW ---
avg_krakow = avg_price(hotels_in_Krakow)
avg_sopot = avg_price(hotels_in_Sopot)

print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_krakow}")
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_sopot}")

# Sprawdzenie gdzie taniej
if avg_krakow < avg_sopot:
    cheaper = "Krakow"
else:
    cheaper = "Sopot"

print(f"Cheaper hotels in: {cheaper}")