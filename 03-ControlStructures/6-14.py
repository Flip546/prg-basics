facebook = False
instagram = False
twitter = False
q1 = input('Do you have Facebook account? (yes/no):')
if q1 == 'yes':
    facebook = True
else:
    facebook = False


q2 = input('Do you have Instagram account? (yes/no): ')
if q2 == 'yes':
    instagram = True
else:
    instagram = False

q3 = input('Do you have twitter account? (yes/no): ')
if q3 == 'yes':
    twitter = True
else:
    twitter = False

print (f'facebook = {facebook}, instagram = {instagram},twitter = {twitter}')
if facebook and instagram and twitter == True:
        print('You are good influencer')