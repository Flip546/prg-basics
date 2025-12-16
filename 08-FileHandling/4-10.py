import csv
try:
    with open('clothing.csv','r',encoding='utf-8')as file:
        reading = csv.DictReader(file)
        for i in reading:
            if float(i['Price']) < 60 and int(i['Stock_Quantity']) < 40:
                nazwa = i['Product_Name']
                cena = i['Price']
                ilosc = i['Stock_Quantity']
                print(f'Produkt: {nazwa} Cena: {cena} Ilosc: {ilosc}')

             
except FileNotFoundError:
    print('NO FILE NAMED THIS WAY BRO,CHECK THE CORRECTNES OF THE NAME')

