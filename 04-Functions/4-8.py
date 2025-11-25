def time_string(hours, minutes, time_format):
    # Formatowanie minut - zawsze muszą mieć dwie cyfry (np. 05, 30)
    minutes_str = f"{minutes:02}"
    
    if time_format == '24':
        # Dla formatu 24h, godziny też formatujemy na 2 cyfry (np. 08, 15)
        return f"{hours:02}:{minutes_str}"
        
    elif time_format == '12':
        # Ustalenie przyrostka AM lub PM
        suffix = "am" if hours < 12 else "pm"
        
        # Konwersja godziny na system 12-godzinny
        if hours == 0:
            h12 = 12  # Północ to 12 am
        elif hours > 12:
            h12 = hours - 12
        else:
            h12 = hours # Przypadki od 1 do 12
            
        # Zwracamy wynik. Zauważ, że w przykładach godziny w formacie 12h 
        # nie mają wiodącego zera (jest 7:30am, a nie 07:30am), więc używamy samego {h12}
        return f"{h12}:{minutes_str}{suffix}"
        
    else:
        return "Nieznany format"

# --- Testowanie funkcji zgodnie z zadaniem ---

print(f"Test 1: {time_string(15, 38, '24')}")   # Oczekiwane: 15:38
print(f"Test 2: {time_string(8, 3, '24')}")     # Oczekiwane: 08:03
print(f"Test 3: {time_string(0, 5, '24')}")     # Oczekiwane: 00:05
print(f"Test 4: {time_string(11, 15, '12')}")   # Oczekiwane: 11:15am
print(f"Test 5: {time_string(0, 7, '12')}")     # Oczekiwane: 12:07am
print(f"Test 6: {time_string(7, 30, '12')}")    # Oczekiwane: 7:30am
print(f"Test 7: {time_string(12, 46, '12')}")   # Oczekiwane: 12:46pm
print(f"Test 8: {time_string(13, 10, '12')}")   # Oczekiwane: 1:10pm
print(f"Test 9: {time_string(19, 2, '12')}")    # Oczekiwane: 7:02pm