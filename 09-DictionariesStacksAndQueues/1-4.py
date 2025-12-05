person = {
   "name": "Marek",
   "hobby": "swimming",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}




person['married'] = False
print (person['married'])
person["name"] = 'Adam'
print(person['name'])
person['gender'] = 'male'
person['phones'] = {'work: 123412231'}
for key,values in person.items():
    print(f'{key}: {values}')



