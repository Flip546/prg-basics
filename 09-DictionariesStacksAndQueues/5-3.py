translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

user_input = input('Enter word to be translated: ')
for i,j in translations.items():
    if user_input in i:
        print(j)
        break
else:
        print('There are no available translations for this word')