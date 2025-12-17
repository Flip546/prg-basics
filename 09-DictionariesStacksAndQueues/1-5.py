countries = [
{"name":"Poland", "population":38000000},
{"name":"Portugal","population":1231234},
{"name":"Spain","population":2313421},
{"name":"Germany","population":213412},
{"name":"Latwia","population":3902123},
]
print('Country     Population')
for i in countries:
    name = i['name']
    pop = i['population']
    print(f'{name:<12}{pop}')