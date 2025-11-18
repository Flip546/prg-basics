code = '0805'
for i in range(3):
         code2 = input('Enter code:')
         if code2 == code:
            print('Acess granted')
            break
         elif i == 2:
               print('Too many attempts')
         else: print('Incorrect code,try again')

    
            