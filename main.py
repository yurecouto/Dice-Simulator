from random import randint
from classes import *


while True:

    print('\033[1;31mDICE SIMULATOR\033[m')
    print("Welcome to the best dice simulator you've ever seen!\n")

    again = 'Y'

    print('Wich dice you wanna roll?')
    print('4 for D4, 6 for D6, 8 for D8')
    print('Press X for quit.')
    dice_type = int(input('>>> '))

    print('')

    # This block is about the D4 dice

    while dice_type == 4:

        d4 = D4(1)

        print(f'Your D4 rolled and returns a >>> \033[1;32m{d4.rolling()}\033[m <<<')
        print('')

        print('Wanna roll it again? [Y/N]')
        again = str(input('>>> '))
        print('')

        if again in 'nN':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

        print('-=' * 30)
        print('')

    # This block is about the D6 dice

    while dice_type == 6:

        d6 = D6(1)

        print(f'Your D6 rolled and returns a >>> \033[1;32m{d6.rolling()}\033[m <<<')
        print('')

        print('Wanna roll it again? [Y/N]')
        again = str(input('>>> '))
        print('')

        if again in 'nN':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

        print('-=' * 30)
        print('')

    # This block is about the D8 dice

    while dice_type == 8:

        d8 = D8(1)

        print(f'Your D8 rolled and returns a >>> \033[1;32m{d8.rolling()}\033[m <<<')
        print('')

        print('Wanna roll it again? [Y/N]')
        again = str(input('>>> '))
        print('')

        if again in 'nN':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

        print('-=' * 30)
        print('')

    # Other configs, about quit and more

    if dice_type in 'xX':
        break

    print('-=' * 30)
    print('')
