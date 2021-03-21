from typing import Type
from dice import *
again = 'Y'
dice_type = 0 

tittle('\033[1;31mDICE SIMULATOR\033[m')

while True:
    print('Wellcome to the best Dice simulator')
    dice_type = int(input('wich kind of dice you want to roll? '))
    print(dice(dice_type))