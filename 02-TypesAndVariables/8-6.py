distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100km: '))
total_fuel_consumption = (distance/100) * fuel_consumption
total_cost = total_fuel_consumption * fuel_price
print(f"Całkowite zużycie paliwa: {total_fuel_consumption:.2f} litrów")
print(f"Całkowity koszt transportu: {total_cost:.2f} zł")