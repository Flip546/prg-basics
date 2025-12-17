import csv
with open('books.csv','r',encoding='utf-8')as file:
    reading = list(csv.DictReader(file))
    def fantasy():
        with open('book_fantasy.txt','w',encoding='utf-8')as file:
            for i in reading:
                if i['Genre'] == 'Fantasy':
                 name = i['Title']
                 auth = i['Author']
                 year = i['Year']

                 file.write(f'Name : {name}\n')
                 file.write(f'Author: {auth}\n')
                 file.write(f'Year: {year}\n')

    def historical():
       with open('historical.txt','w',encoding='utf-8')as file:
          for i in reading:
             if i['Genre'] == 'Historical':
                name = i['Title']
                auth = i['Author']
                year = i['Year']

                file.write(f'Name: {name}\nAuthor: {auth}\nYear: {year}\n')
    def Romance():
       with open('romance.txt','w',encoding='utf-8')as file:
          for i in reading:
             if i['Genre'] == 'Romance':
                name = i['Title']
                auth = i['Author']
                year = i['Year']

                file.write(f'Name: {name}\nAuthor: {auth}\nYear: {year}\n')
    def classic():
       with open('classic.txt','w',encoding='utf-8')as file:
          for i in reading:
             if i['Genre'] == 'Classic':
                name = i['Title']
                auth = i['Author']
                year = i['Year']

                file.write(f'Name: {name}\nAuthor: {auth}\nYear: {year}\n')

 

    fantasy()
    historical()
    Romance()
    classic()




            


          

