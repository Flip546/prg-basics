import random 
dice_roll_ = random.randint(1,6)
dice_roll_ok= dice_roll_ in (1,6)
print(f'Dice rolled: {dice_roll_}')
print(f'If special number: {dice_roll_ok}')