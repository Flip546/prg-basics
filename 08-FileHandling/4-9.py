import csv

print('GRAPHIC DESIGNERS')
print('=================')
try:
    with open('it_company.csv', 'r',encoding='utf-8')as file:
        reader = csv.DictReader(file)
        for i in reader:
            if i['Job Title']== 'Graphic Designer':

                name = i['First Name']
                Lastname = i['Last Name']
                mail = i['Email']

                print(f'{name} {Lastname}, {mail}')
except FileNotFoundError:
    print('File not found')