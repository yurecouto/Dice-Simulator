from dice import *

again = 'Y'
dice_type = 0 

tittle('\033[1;31mDICE SIMULATOR\033[m')
print("Wellcome to the best dice simulator you've ever seen!\n")

while True:
    if again.upper() == 'N':
        break

    elif again.upper() == 'Y':
        dice_type = int(input('Wich kind of dice you want to roll? '))
        dice(dice_type)

    else:
        print('\033[1;31mERROR\033[m')
        print('You can only type y for yes or n for not')


    again = input('Wanna play again? [y/n] ')
