with open('vehicle.txt','r')as file:
    content = file.read().split()
   
import csv

with open('province.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        litera = row['Letter']
        woj = row['Name']
        for word in content:
            if word.startswith(litera):
                print(f'Rejstracja {word} jest z {woj}')