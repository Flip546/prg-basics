with open('Result.txt', 'w',encoding='utf-8')as file:
    for i in range(1,101):
        tekst = f'{i},{i**2},{i**3}\n'
        file.write(tekst)