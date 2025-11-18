Number = (input('Enter EAN-13 article number: '))
if len(Number) == 13 and  Number[0:3] == '590':
    print ('Article number is correct')
    print ('Article manufactured in Poland.')
elif len (Number) != 13:
    print ('Article number is incorrect. EAN-13 number must have 13 digits.')
elif len (Number) == 13:
    print('Article number is correct')
    print('Article not manufactured in Poland.')

    