from dice import *

dice_type = 0

while True:

    tittle('\033[1;31mDICE SIMULATOR\033[m')
    print("Welcome to the best dice simulator you've ever seen!\n")

    again = 'Y'
    print('1 - Press "A" for the free dice game-mode.')
    print('2 - or "B" for the dual D6 game-mode.')
    print('3 - you can press "X" for quit.')
    game_mode = input(f'Choose your game-mode [A, B or X]: ')

    while game_mode.upper() == 'A':
        
        dice_type = int(input('Which kind of dice you want to roll? '))
        free_dice(dice_type)

        again = input('Play again? [Y/N] ')

        if again.upper() == 'N':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

    while game_mode.upper() == 'B':

        dual_d6()

        again = input('Play again? [Y/N] ')

        if again.upper() == 'N':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

    if game_mode.upper() == 'X':
        break

    elif game_mode.upper() not in 'ABX':
        print('\033[1;31mERROR\033[m')
        print('You can only type "A", "B" or "X"')

sleeping('Closing')
print('\033[1;31mTHE END.\033[m')

'''print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')'''
